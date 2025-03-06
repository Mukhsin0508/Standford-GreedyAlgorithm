import speedtest

st = speedtest.Speedtest()
st.get_best_server()  # Manually fetch best server
download_speed = st.download()
upload_speed = st.upload()

print(f"Download Speed: {download_speed / 1_000_000:.2f} Mbps")
print(f"Upload Speed: {upload_speed / 1_000_000:.2f} Mbps")
