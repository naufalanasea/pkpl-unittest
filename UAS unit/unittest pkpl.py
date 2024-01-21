from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Buka halaman web
driver.get("https://hastamu.000webhostapp.com/")

# Set ukuran jendela browser (opsional)
driver.set_window_size(1122, 816)

# Klik link "Kalkulator"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Kalkulator"))).click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button:nth-child(8)"))).click()  # Klik angka 4
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button:nth-child(9)"))).click()  # Klik angka 5
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".operator:nth-child(3)"))).click()  # Klik operator Kali
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button:nth-child(8)"))).click()  # Klik angka 3
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button:nth-child(9)"))).click()  # Klik angka 5
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".equal-sign"))).click()  # Klik tombol sama dengan


# Dapatkan hasil kalkulator
result_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".calculator-screen")))

# Ambil teks hasil kalkulator
calculator_result = result_element.get_attribute("value")

# Klik tombol "All Clear"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".all-clear"))).click()

# Klik link "Home"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Home"))).click()

# Periksa hasil kalkulator

if calculator_result == "2025":
    print("Hasil Pemeriksaan Benar, Pengujian Berhasil")
else:
    print(f"Hasil Pemeriksaan Salah. Hasil seharusnya: 2025, Hasil pada pengujian: {calculator_result}")

driver.quit()
#uas
