# Prereq

Machine needs to support Wake on LAN

Look for Advanced Power Management features in UEFI


# Build

```
docker compose up -d --build --force-recreate 
```

It runs a flask app on port 5090 which is mapped via internal reverse proxy to a local DNS name https://reset.i.cloudgenius.app


# Run WakeOnLanWeb
Web UI to control power state of a Windows PC

Supports the following features:

- Turn on
- Restart
- Turn off
