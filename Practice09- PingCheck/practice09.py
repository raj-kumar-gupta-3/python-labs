import subprocess
host = input("Enter an IP or website to ping: ")
result = subprocess.run(
  ["ping", "-c", "2", host],
  capture_output=True
  text=True
  )
if result,returncode == 0:
print(host, "is reachable")
else:
print(host, "is not reachable")
