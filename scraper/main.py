import sys
import subprocess
import os
import signal

PID_FILE = "bacara.pid"


def is_pid_running(pid):
    try:
        if os.name == 'nt':
            # En Windows, esto lanza una excepción si el proceso no existe
            import psutil
            return psutil.pid_exists(pid)
        else:
            os.kill(pid, 0)
            return True
    except Exception:
        return False


def start_bacara():
    if os.path.exists(PID_FILE):
        with open(PID_FILE, "r") as f:
            try:
                pid = int(f.read())
            except Exception:
                pid = None
        if pid and is_pid_running(pid):
            print("[INFO] El proceso ya está iniciado. Usa stop para detenerlo primero.")
            return
        else:
            print("[WARN] El archivo PID existe pero el proceso no está activo. Eliminando PID y arrancando...")
            os.remove(PID_FILE)
    # Lanzar bacara.py como proceso independiente (detached)
    if os.name == 'nt':  # Windows
        DETACHED = subprocess.CREATE_NEW_CONSOLE
        process = subprocess.Popen([
            sys.executable, "bacara.py"
        ], creationflags=DETACHED, close_fds=True)
    else:
        process = subprocess.Popen([
            sys.executable, "bacara.py"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, preexec_fn=os.setpgrp)
    with open(PID_FILE, "w") as f:
        f.write(str(process.pid))
    print(f"[START] bacara.py iniciado con PID {process.pid}")


def stop_bacara():
    if not os.path.exists(PID_FILE):
        print("[INFO] No hay proceso en ejecución para detener.")
        return
    with open(PID_FILE, "r") as f:
        pid = int(f.read())
    try:
        if os.name == 'nt':  # Windows
            os.kill(pid, signal.SIGTERM)
        else:
            os.kill(pid, signal.SIGTERM)
        print(f"[STOP] Proceso bacara.py con PID {pid} detenido.")
    except Exception as e:
        print(f"[ERROR] No se pudo detener el proceso: {e}")
    os.remove(PID_FILE)


def main():
    if len(sys.argv) == 1:
        # Sin argumentos: comportarse como 'start'
        start_bacara()
        return
    if len(sys.argv) == 2 and sys.argv[1] in ["start", "stop"]:
        if sys.argv[1] == "start":
            start_bacara()
        elif sys.argv[1] == "stop":
            stop_bacara()
        return
    print("Uso: python main.py [start|stop]")


if __name__ == "__main__":
    main()
