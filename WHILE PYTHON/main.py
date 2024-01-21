from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://localhost/pkpl/Dosen/login.php")

# Tunggu hingga tombol login dapat diklik
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login-button")))

# Masukkan username
username_input = driver.find_element(By.NAME, "username")
username_input.send_keys("admin")

# Masukkan password
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys("admin")

# Klik tombol login
driver.find_element(By.CSS_SELECTOR, "#login-button").click()

# Periksa apakah pengguna berhasil masuk ke halaman dashboard dosen
assert driver.current_url == "http://localhost/pkpl/Dosen/index.php", "Pengujian login gagal"
print("Pengujian login berhasil")

driver.quit()