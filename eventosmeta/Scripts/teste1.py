from webdriver_manager.chrome import ChromeDriverManager

driver_path = ChromeDriverManager().install()
print(f"ChromeDriver instalado em: {driver_path}")



