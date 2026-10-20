import subprocess

result = subprocess.run(
    ["ping", "-n", "4", "127.0.0.1"],
     capture_output=True,
     text=True

)
print("Output type:", type(result.stdout))
print("Return code:", result.returncode)
print("Output:", result.stdout)