import time
from playwright.sync_api import sync_playwright

# --- Credenciales ---
EMAIL = "tatianatorres.o@hotmail.com"
PASSWORD = "160120Juan!"
LOGIN_URL = "https://stake.com.co/es/casino/juego/baccarat"

def save_page_content(page, filename="page_content.html"):
    """Guarda el contenido HTML de la página para depuración."""
    try:
        html = page.content()
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"--- [DEBUG] Contenido HTML guardado en '{filename}' ---")
    except Exception as e:
        print(f"Error al guardar el contenido de la página: {e}")

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    try:
        print("[PASO 1] Navegando a la URL...")
        page.goto(LOGIN_URL, timeout=120000, wait_until="domcontentloaded")
        print("[PASO 1] Navegación completada.")

        # Guardamos el HTML inicial para tener una referencia
        save_page_content(page, filename="initial_page_content.html")
        
        print("[PASO 2] Buscando y haciendo clic en 'Iniciar sesión' para abrir el modal...")
        # Selector basado en tu sugerencia: <button class="... variant-link">Iniciar sesión</button>
        login_button_selector = 'button.variant-link:has-text("Iniciar sesión")'
        page.locator(login_button_selector).click()
        print("[PASO 2] Clic realizado en 'Iniciar sesión'.")

        print("[PASO 3] Esperando a que el formulario de login esté visible...")
        # Selector actualizado basado en el HTML que encontraste.
        # Busca un 'form' dentro del modal que contiene el título 'Iniciar sesión'.
        login_form_selector = 'div.modal-content:has(h1:text("Iniciar sesión")) form'
        login_form = page.locator(login_form_selector)
        login_form.wait_for(timeout=100000)
        print("[PASO 3] Formulario de login visible.")
        
        print("[PASO 4] Llenando credenciales...")
        login_form.locator('input[name="username"]').fill(EMAIL)
        print("[PASO 4] Email llenado.")
        login_form.locator('input[name="password"]').fill(PASSWORD)
        print("[PASO 4] Contraseña llenada.")
        
        print("[PASO 5] Enviando formulario...")
        login_form.locator('button[type="submit"]').click()
        print("[PASO 5] Formulario enviado.")

        print("[PASO 6] Verificando que el juego ha cargado (buscando 'Juego real')...")
        # Selector actualizado basado en tu feedback.
        real_play_button_selector = 'button.btn-primary:has-text("Juego real")'
        real_play_button = page.locator(real_play_button_selector)
        real_play_button.wait_for(timeout=100000) # Damos tiempo extra para que cargue el juego.
        print("[PASO 6] Botón 'Juego real' encontrado.")

        print("[PASO 7] Haciendo clic en 'Juego real'...")
        real_play_button.click()
        print("[PASO 7] Clic realizado en 'Juego real'.")

        print("[PASO 8] Esperando a que el botón 'MULTIJUEGO' esté disponible...")
        # Selector basado en el HTML que proporcionaste. Busca el contenedor del botón.
        multijuego_button_selector = 'div.bs_bt:has(div:text("MULTIJUEGO"))'
        multijuego_button = page.locator(multijuego_button_selector)
        multijuego_button.wait_for(timeout=100000) # Tiempo para que cargue la interfaz del juego
        print("[PASO 8] Botón 'MULTIJUEGO' encontrado.")

        print("[PASO 9] Haciendo clic en 'MULTIJUEGO'...")
        multijuego_button.click()
        print("[PASO 9] ¡ÉXITO! Clic realizado.")
        
        print("\nTarea completada. Pausa de 30 segundos para revisión.")
        time.sleep(30)

    except Exception as e:
        print(f"\n[ERROR] El script falló: {e}")
        print("[DEBUG] Guardando el contenido HTML en el momento del error...")
        save_page_content(page, filename="error_page_content.html")
        print("[INFO] Revisa 'initial_page_content.html' y 'error_page_content.html' para comparar.")

    finally:
        print("Cerrando navegador.")
        browser.close()

def main():
    with sync_playwright() as playwright:
        run(playwright)

if __name__ == "__main__":
    main() 