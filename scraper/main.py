import time
import sys
from playwright.sync_api import sync_playwright

# --- Credenciales ---
EMAIL = "tatianatorres.o@hotmail.com"
PASSWORD = "160120Juan!"
LOGIN_URL = "https://stake.com.co/es"

def save_page_content(page, filename="page_content.html"):
    """Guarda el contenido HTML de la página para depuración."""
    try:
        html = page.content()
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"--- [DEBUG] Contenido HTML guardado en '{filename}' ---", flush=True)
    except Exception as e:
        print(f"Error al guardar el contenido de la página: {e}", flush=True)

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    try:
        print("[PASO 1] Navegando a la URL de inicio...", flush=True)
        page.goto(LOGIN_URL, timeout=120000, wait_until="domcontentloaded")
        print("[PASO 1] Navegación completada.", flush=True)

        # Guardamos el HTML inicial para tener una referencia
        save_page_content(page, filename="initial_page_content.html")
        
        print("[PASO 2] Buscando y haciendo clic en 'Iniciar sesión' para abrir el modal...", flush=True)
        login_button_selector = 'button.variant-link:has-text("Iniciar sesión")'
        page.locator(login_button_selector).click()
        print("[PASO 2] Clic realizado en 'Iniciar sesión'.", flush=True)

        print("[PASO 3] Esperando a que el formulario de login esté visible...", flush=True)
        login_form_selector = 'div.modal-content:has(h1:text("Iniciar sesión")) form'
        login_form = page.locator(login_form_selector)
        login_form.wait_for(timeout=10000)
        print("[PASO 3] Formulario de login visible.", flush=True)
        
        print("[PASO 4] Llenando credenciales...", flush=True)
        login_form.locator('input[name="username"]').fill(EMAIL)
        print("[PASO 4] Email llenado.", flush=True)
        login_form.locator('input[name="password"]').fill(PASSWORD)
        print("[PASO 4] Contraseña llenada.", flush=True)
        
        print("[PASO 5] Enviando formulario...", flush=True)
        login_form.locator('button[type="submit"]').click()
        print("[PASO 5] Formulario enviado.", flush=True)
        
        print("[PASO 6] Navegando a la sección 'Casino'...", flush=True)
        casino_selector = 'a.page-header__sidebar-link:has-text("Casino")'
        page.locator(casino_selector).wait_for(timeout=60000)
        page.locator(casino_selector).click()
        print("[PASO 6] Clic en 'Casino' realizado.", flush=True)

        print("[PASO 7] Dando clic en 'Pragmatic Play'...", flush=True)
        pragmatic_selector = 'img[alt="pragmatic_play_live"]'
        page.locator(pragmatic_selector).wait_for(timeout=60000)
        page.locator(pragmatic_selector).click()
        print("[PASO 7] Clic en 'Pragmatic Play' realizado.", flush=True)
        
        print("[PASO 8] Ingresando a 'Baccarat' de Pragmatic Play Live...", flush=True)
        baccarat_selector = 'a[href="/es/casino/juego/baccarat"]:has(span:text("Pragmatic Play Live"))'
        baccarat_game = page.locator(baccarat_selector)
        baccarat_game.wait_for(timeout=60000)
        baccarat_game.click()
        print("[PASO 8] Clic en 'Baccarat' realizado.", flush=True)

        print("[PASO 9] Haciendo clic en 'Juego real'...", flush=True)
        real_play_button_selector = 'button.btn-primary:has-text("Juego real")'
        real_play_button = page.locator(real_play_button_selector)
        real_play_button.wait_for(timeout=100000)
        real_play_button.click()
        print("[PASO 9] Clic realizado en 'Juego real'.", flush=True)

        print("[PASO 10] Esperando a que el juego cargue completamente...", flush=True)
        time.sleep(25)  # Más tiempo para que cargue completamente
        
        # Guardar HTML completo para análisis
        print("[DEBUG] Guardando HTML completo de la página del juego...", flush=True)
        save_page_content(page, filename="game_page_complete.html")
        
        print("[PASO 10] Buscando el botón 'Menu' DENTRO del iframe del juego...", flush=True)
        
        menu_found = False
        
        # ESTRATEGIA MEJORADA: Hacer clic específicamente DENTRO del iframe del juego
        print("[DEBUG] Obteniendo coordenadas exactas del iframe del juego...", flush=True)
        try:
            # Cerrar cualquier menú lateral que pueda estar abierto
            print("[DEBUG] Cerrando menús laterales que puedan estar abiertos...", flush=True)
            page.keyboard.press('Escape')
            time.sleep(1)
            
            # Obtener información precisa del iframe del juego
            game_iframe_info = page.evaluate("""
                () => {
                    let gameFrame = document.querySelector('iframe.game');
                    if (gameFrame) {
                        let rect = gameFrame.getBoundingClientRect();
                        return {
                            found: true,
                            x: rect.x,
                            y: rect.y,
                            width: rect.width,
                            height: rect.height,
                            src: gameFrame.src.substring(0, 100)
                        };
                    }
                    return { found: false };
                }
            """)
            
            if game_iframe_info['found']:
                iframe_x = game_iframe_info['x']
                iframe_y = game_iframe_info['y']
                iframe_width = game_iframe_info['width']
                iframe_height = game_iframe_info['height']
                
                print(f"[DEBUG] Iframe del juego encontrado:", flush=True)
                print(f"[DEBUG] - Posición: x={iframe_x:.1f}, y={iframe_y:.1f}", flush=True)
                print(f"[DEBUG] - Tamaño: w={iframe_width:.1f}, h={iframe_height:.1f}", flush=True)
                print(f"[DEBUG] - Src: {game_iframe_info['src']}", flush=True)
                
                # Tomar captura ANTES de hacer cualquier clic
                print("[DEBUG] Tomando captura inicial del juego...", flush=True)
                page.screenshot(path="game_initial_state.png")
                
                # Coordenadas exactas que funcionaron según before_lobby_click_1_5.png
                menu_x = iframe_x + iframe_width - 35
                menu_y = iframe_y + 35
                
                print(f"\n[DEBUG] Haciendo clic en el menú en coordenadas: ({menu_x:.1f}, {menu_y:.1f})", flush=True)
                
                # Asegurar que no hay menús abiertos antes del clic
                page.keyboard.press('Escape')
                time.sleep(2)
                
                # Hacer clic en el menú
                page.mouse.click(menu_x, menu_y)
                time.sleep(3)  # Esperar a que se abra el menú
                
                # Coordenadas exactas que funcionaron para el lobby
                lobby_x = menu_x - 240  # 240px a la izquierda del menú
                lobby_y = menu_y + 45   # 45px abajo del menú
                
                print(f"[DEBUG] Haciendo clic en Lobby en coordenadas: ({lobby_x:.1f}, {lobby_y:.1f})", flush=True)
                page.mouse.click(lobby_x, lobby_y)
                
                # Esperar a que cargue el lobby
                print("[DEBUG] Esperando a que cargue el lobby...", flush=True)
                time.sleep(8)
                
                # Tomar captura después de la carga del lobby
                page.screenshot(path="after_lobby_load.png")
                
                print("[DEBUG] Buscando 'Multijuego de Bacará'...", flush=True)
                
                # Coordenadas absolutas para la primera tarjeta (superior izquierda)
                # Basado en la imagen, la primera tarjeta está aproximadamente en estas coordenadas
                first_card_x = iframe_x + 150  # Aproximadamente 150px desde el borde izquierdo del iframe
                first_card_y = iframe_y + 150  # Aproximadamente 150px desde el borde superior del iframe
                
                print(f"[DEBUG] Intentando clic en primera tarjeta en: ({first_card_x:.1f}, {first_card_y:.1f})", flush=True)
                
                # Tomar captura antes del clic
                page.screenshot(path="before_card_click.png")
                
                # Hacer clic en la posición de la primera tarjeta
                page.mouse.click(first_card_x, first_card_y)
                
                # Esperar a que se procese el clic
                print("[DEBUG] Esperando a que cargue el juego...", flush=True)
                time.sleep(5)
                
                # Tomar captura después del clic
                page.screenshot(path="after_card_click.png")
                
                print("[ÉXITO] Clic realizado en la primera tarjeta (Multijuego de Bacará)", flush=True)
                
                # Verificar si el juego cargó correctamente
                time.sleep(3)
                page.screenshot(path="final_game_state.png")
                print("--- [DEBUG] Captura final del juego guardada ---", flush=True)
                
            else:
                print("[ERROR] No se pudo encontrar el iframe del juego", flush=True)
                
        except Exception as e:
            print(f"[ERROR] Error en la estrategia mejorada: {e}", flush=True)

        if menu_found:
            print("\n[PASO 11] ¡ÉXITO TOTAL! Menú del juego encontrado y 'Lobby' clickeado.", flush=True)
            
            # Esperar para que se complete la acción
            time.sleep(5)
            
            # PASO FINAL: Hacer clic en "Multijuego de Bacará"
            print("[PASO 13] Esperando a que cargue el lobby y buscando 'Multijuego de Bacará'...", flush=True)
            
            # Esperar más tiempo para que el lobby cargue completamente
            time.sleep(10)
            
            # Tomar captura del lobby
            page.screenshot(path="lobby_loaded.png")
            print("--- [DEBUG] Captura del lobby guardada en 'lobby_loaded.png' ---", flush=True)
            
            # Buscar "Multijuego de Bacará" con múltiples estrategias
            baccarat_found = False
            
            # ESTRATEGIA 1: Usar el selector específico del HTML proporcionado
            print("[DEBUG] Método 1: Buscando con selector específico...", flush=True)
            try:
                baccarat_selector = 'span[data-testid="tile-container-title"]:has-text("Multijuego de Bacará")'
                baccarat_element = page.locator(baccarat_selector)
                baccarat_element.wait_for(timeout=10000)
                
                # Hacer clic en el elemento padre (la tarjeta completa)
                baccarat_card = baccarat_element.locator('..')  # Elemento padre
                baccarat_card.click()
                
                print("[PASO 13] ¡ÉXITO! Clic en 'Multijuego de Bacará' realizado!", flush=True)
                baccarat_found = True
                
            except Exception as e:
                print(f"[DEBUG] Método 1 falló: {str(e)[:100]}...", flush=True)
            
            # ESTRATEGIA 2: Buscar por texto directo
            if not baccarat_found:
                print("[DEBUG] Método 2: Buscando por texto directo...", flush=True)
                try:
                    baccarat_selectors = [
                        ':has-text("Multijuego de Bacará")',
                        ':has-text("Multijuego")',
                        ':has-text("Bacará")',
                        'span:has-text("Multijuego de Bacará")',
                        'div:has-text("Multijuego de Bacará")',
                        '[data-testid="tile-container-title"]'
                    ]
                    
                    for selector in baccarat_selectors:
                        try:
                            print(f"[DEBUG] Probando selector: {selector}", flush=True)
                            element = page.locator(selector)
                            element.wait_for(timeout=3000)
                            element.click()
                            print(f"[PASO 13] ¡ÉXITO! Clic realizado con selector: {selector}", flush=True)
                            baccarat_found = True
                            break
                        except:
                            continue
                            
                except Exception as e:
                    print(f"[DEBUG] Método 2 falló: {e}", flush=True)
            
            # ESTRATEGIA 3: Buscar con JavaScript
            if not baccarat_found:
                print("[DEBUG] Método 3: Buscando con JavaScript...", flush=True)
                try:
                    baccarat_js_result = page.evaluate("""
                        () => {
                            let elements = document.querySelectorAll('*');
                            for (let elem of elements) {
                                let text = elem.innerText || elem.textContent || '';
                                if (text.includes('Multijuego de Bacará') || 
                                    text.includes('Multijuego') || 
                                    text.includes('Bacará')) {
                                    let rect = elem.getBoundingClientRect();
                                    if (rect.width > 0 && rect.height > 0) {
                                        return {
                                            found: true,
                                            x: rect.x + rect.width/2,
                                            y: rect.y + rect.height/2,
                                            text: text.trim()
                                        };
                                    }
                                }
                            }
                            return { found: false };
                        }
                    """)
                    
                    if baccarat_js_result['found']:
                        print(f"[ÉXITO] 'Multijuego de Bacará' encontrado: '{baccarat_js_result['text'][:50]}'", flush=True)
                        print(f"[DEBUG] Coordenadas: ({baccarat_js_result['x']}, {baccarat_js_result['y']})", flush=True)
                        page.mouse.click(baccarat_js_result['x'], baccarat_js_result['y'])
                        print("[PASO 13] ¡ÉXITO! Clic en 'Multijuego de Bacará' realizado con JavaScript!", flush=True)
                        baccarat_found = True
                    else:
                        print("[DEBUG] No se encontró 'Multijuego de Bacará' con JavaScript", flush=True)
                        
                except Exception as e:
                    print(f"[DEBUG] Método 3 falló: {e}", flush=True)
            
            # ESTRATEGIA 4: Buscar todas las tarjetas/tiles y hacer clic en la primera
            if not baccarat_found:
                print("[DEBUG] Método 4: Buscando todas las tarjetas disponibles...", flush=True)
                try:
                    # Buscar elementos que parezcan tarjetas de juego
                    tiles = page.locator('div[class*="kx_"], div[data-testid*="tile"], .tile, .card').all()
                    print(f"[DEBUG] Encontradas {len(tiles)} tarjetas potenciales", flush=True)
                    
                    for i, tile in enumerate(tiles[:5]):  # Solo las primeras 5
                        try:
                            tile_text = tile.inner_text()
                            print(f"[DEBUG] Tarjeta {i+1}: '{tile_text[:50]}'", flush=True)
                            
                            if 'bacará' in tile_text.lower() or 'multijuego' in tile_text.lower():
                                print(f"[ÉXITO] Tarjeta de Bacará encontrada: '{tile_text[:30]}'", flush=True)
                                tile.click()
                                print("[PASO 13] ¡ÉXITO! Clic en tarjeta de Bacará realizado!", flush=True)
                                baccarat_found = True
                                break
                        except Exception as e:
                            print(f"[DEBUG] Error con tarjeta {i+1}: {e}", flush=True)
                            continue
                            
                except Exception as e:
                    print(f"[DEBUG] Método 4 falló: {e}", flush=True)
            
            if baccarat_found:
                print("[PASO 14] ¡PROCESO COMPLETADO! Se ha hecho clic en 'Multijuego de Bacará'", flush=True)
                time.sleep(5)  # Esperar a que cargue el juego final
                page.screenshot(path="final_baccarat_game.png")
                print("--- [DEBUG] Captura final del juego guardada en 'final_baccarat_game.png' ---", flush=True)
            else:
                print("[DEBUG] No se pudo encontrar 'Multijuego de Bacará'. Guardando HTML del lobby...", flush=True)
                save_page_content(page, filename="lobby_content.html")
            
            # Tomar captura de pantalla final
            print("[DEBUG] Tomando captura de pantalla final...", flush=True)
            try:
                page.screenshot(path="final_success.png")
                print("--- [DEBUG] Captura final de éxito guardada en 'final_success.png' ---", flush=True)
            except Exception as e:
                print(f"[DEBUG] Error tomando captura final: {e}", flush=True)
        
        else:
            print("[ERROR] No se pudo encontrar el menú del juego o 'Lobby'.", flush=True)
            
            # Tomar captura del estado final aunque no haya funcionado
            try:
                page.screenshot(path="final_failed.png")
                print("--- [DEBUG] Captura del intento fallido guardada en 'final_failed.png' ---", flush=True)
            except Exception as e:
                print(f"[DEBUG] Error tomando captura del fallo: {e}", flush=True)
        
        # PASO ADICIONAL: Hacer clic en botón de pantalla completa
        print("\n[PASO 15] Intentando hacer clic en el botón de pantalla completa...", flush=True)
        try:
            # Esperar un poco más para asegurar que todo esté cargado
            time.sleep(3)
            
            # Tomar captura antes del clic en pantalla completa
            page.screenshot(path="before_fullscreen_click.png")
            print("--- [DEBUG] Captura antes del clic en pantalla completa guardada ---", flush=True)
            
            # Obtener las coordenadas del iframe del juego nuevamente
            game_iframe_info = page.evaluate("""
                () => {
                    let gameFrame = document.querySelector('iframe.game');
                    if (gameFrame) {
                        let rect = gameFrame.getBoundingClientRect();
                        return {
                            found: true,
                            x: rect.x,
                            y: rect.y,
                            width: rect.width,
                            height: rect.height
                        };
                    }
                    return { found: false };
                }
            """)
            
            if game_iframe_info['found']:
                iframe_x = game_iframe_info['x']
                iframe_y = game_iframe_info['y']
                iframe_width = game_iframe_info['width']
                iframe_height = game_iframe_info['height']
                
                # Coordenadas del botón menú (que ya sabemos que funcionan)
                menu_x = iframe_x + iframe_width - 35
                menu_y = iframe_y + 35
                
                print(f"[DEBUG] Coordenadas del botón menú: ({menu_x:.1f}, {menu_y:.1f})", flush=True)
                
                # Probar diferentes coordenadas para el botón de pantalla completa
                # Basándome en tu descripción: más arriba y más a la derecha
                fullscreen_positions = [
                    (menu_x + 5, menu_y - 5),   # 5px derecha, 5px arriba
                    (menu_x + 10, menu_y - 10), # 10px derecha, 10px arriba
                    (menu_x + 15, menu_y - 5),  # 15px derecha, 5px arriba
                    (menu_x + 5, menu_y - 15),  # 5px derecha, 15px arriba
                    (menu_x + 10, menu_y - 5),  # 10px derecha, 5px arriba
                    (menu_x + 15, menu_y - 10), # 15px derecha, 10px arriba
                    (menu_x + 20, menu_y - 10), # 20px derecha, 10px arriba
                    (menu_x + 10, menu_y - 20), # 10px derecha, 20px arriba
                ]
                
                for i, (fs_x, fs_y) in enumerate(fullscreen_positions, 1):
                    print(f"\n[DEBUG] Intento {i}: Probando coordenadas ({fs_x:.1f}, {fs_y:.1f})", flush=True)
                    
                    # Hacer clic en la posición
                    page.mouse.click(fs_x, fs_y)
                    
                    # Esperar a ver si algo cambió
                    time.sleep(2)
                    
                    # Tomar captura después del clic
                    page.screenshot(path=f"fullscreen_attempt_{i}.png")
                    print(f"--- [DEBUG] Captura del intento {i} guardada en 'fullscreen_attempt_{i}.png' ---", flush=True)
                    
                    # Verificar si la pantalla cambió a modo completo
                    # Esto se puede hacer verificando el tamaño del iframe o cambios en la página
                    new_iframe_info = page.evaluate("""
                        () => {
                            let gameFrame = document.querySelector('iframe.game');
                            if (gameFrame) {
                                let rect = gameFrame.getBoundingClientRect();
                                return {
                                    width: rect.width,
                                    height: rect.height,
                                    isFullscreen: rect.width > 1200 || rect.height > 600
                                };
                            }
                            return { width: 0, height: 0, isFullscreen: false };
                        }
                    """)
                    
                    print(f"[DEBUG] Tamaño del iframe después del clic: {new_iframe_info['width']:.1f}x{new_iframe_info['height']:.1f}", flush=True)
                    
                    if new_iframe_info['isFullscreen']:
                        print(f"[ÉXITO] ¡Pantalla completa activada en el intento {i}!", flush=True)
                        
                        # Tomar múltiples capturas con diferentes intervalos para asegurar capturar la pantalla completa
                        print("[DEBUG] Tomando múltiples capturas de la pantalla completa...", flush=True)
                        
                        # Captura inmediata
                        page.screenshot(path=f"fullscreen_immediate_{i}.png")
                        print(f"--- [DEBUG] Captura inmediata guardada en 'fullscreen_immediate_{i}.png' ---", flush=True)
                        
                        # Esperar y tomar capturas adicionales
                        for delay in [1, 2, 3, 5]:
                            time.sleep(delay)
                            page.screenshot(path=f"fullscreen_after_{delay}s_{i}.png")
                            print(f"--- [DEBUG] Captura después de {delay}s guardada en 'fullscreen_after_{delay}s_{i}.png' ---", flush=True)
                            
                            # Verificar el tamaño del iframe en cada captura
                            current_iframe_info = page.evaluate("""
                                () => {
                                    let gameFrame = document.querySelector('iframe.game');
                                    if (gameFrame) {
                                        let rect = gameFrame.getBoundingClientRect();
                                        return {
                                            width: rect.width,
                                            height: rect.height,
                                            x: rect.x,
                                            y: rect.y
                                        };
                                    }
                                    return { width: 0, height: 0, x: 0, y: 0 };
                                }
                            """)
                            
                            print(f"[DEBUG] Después de {delay}s - Iframe: {current_iframe_info['width']:.1f}x{current_iframe_info['height']:.1f} en ({current_iframe_info['x']:.1f}, {current_iframe_info['y']:.1f})", flush=True)
                        
                        # Tomar captura final en pantalla completa
                        time.sleep(2)
                        page.screenshot(path="final_fullscreen_success.png")
                        print("--- [DEBUG] Captura final en pantalla completa guardada ---", flush=True)
                        
                        # Información adicional del estado final
                        final_info = page.evaluate("""
                            () => {
                                let gameFrame = document.querySelector('iframe.game');
                                if (gameFrame) {
                                    let rect = gameFrame.getBoundingClientRect();
                                    return {
                                        width: rect.width,
                                        height: rect.height,
                                        x: rect.x,
                                        y: rect.y,
                                        windowWidth: window.innerWidth,
                                        windowHeight: window.innerHeight
                                    };
                                }
                                return null;
                            }
                        """)
                        
                        if final_info:
                            print(f"[DEBUG] ESTADO FINAL - Iframe: {final_info['width']:.1f}x{final_info['height']:.1f}", flush=True)
                            print(f"[DEBUG] ESTADO FINAL - Posición: ({final_info['x']:.1f}, {final_info['y']:.1f})", flush=True)
                            print(f"[DEBUG] ESTADO FINAL - Ventana: {final_info['windowWidth']}x{final_info['windowHeight']}", flush=True)
                        
                        break
                    else:
                        print(f"[DEBUG] Intento {i} no activó pantalla completa, continuando...", flush=True)
                        
                        # Si no fue el último intento, esperar un poco antes del siguiente
                        if i < len(fullscreen_positions):
                            time.sleep(1)
                
                # Tomar captura final del proceso de pantalla completa
                page.screenshot(path="final_fullscreen_process.png")
                print("--- [DEBUG] Captura final del proceso de pantalla completa guardada ---", flush=True)
                
            else:
                print("[DEBUG] No se pudo obtener información del iframe para el botón de pantalla completa", flush=True)
                
        except Exception as e:
            print(f"[DEBUG] Error en el proceso de pantalla completa: {e}", flush=True)
            # Tomar captura del error
            try:
                page.screenshot(path="fullscreen_error.png")
                print("--- [DEBUG] Captura del error en pantalla completa guardada ---", flush=True)
            except:
                pass
        
        print("\nTarea completada. El navegador permanecerá abierto por 60 segundos.", flush=True)
        print("Revisa las capturas de pantalla generadas para ver exactamente dónde se hizo clic.", flush=True)
        print("Puedes ver el navegador ahora para verificar el resultado.", flush=True)
        
        # Mantener el navegador abierto por más tiempo
        for i in range(60, 0, -10):
            print(f"Cerrando en {i} segundos... (presiona Ctrl+C para mantener abierto)", flush=True)
            time.sleep(10)

    except KeyboardInterrupt:
        print("\n[INFO] Interrupción del usuario. Manteniendo navegador abierto.", flush=True)
        print("Presiona Enter para cerrar el navegador...", flush=True)
        input()
    except Exception as e:
        print(f"\n[ERROR] El script falló: {e}", flush=True)
        print("[DEBUG] Guardando el contenido HTML en el momento del error...", flush=True)
        save_page_content(page, filename="error_page_content.html")
        print("[INFO] Revisa los archivos HTML para debug.", flush=True)

    finally:
        try:
            print("Cerrando navegador...", flush=True)
            browser.close()
        except:
            print("Navegador ya cerrado o error al cerrar.", flush=True)

def main():
    with sync_playwright() as playwright:
        run(playwright)

if __name__ == "__main__":
    main() 