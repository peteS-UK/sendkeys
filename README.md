# Home Assistant Key Send Service

This simple integration adds an action for Home Assistant which allows you to send key strokes over tcp/ip to a listening server

```yaml
action: sendkeys_service.sendkeys
data:
  serverPort: "65432"
  serverIp: 192.168.1.35
  keyname: playing
```
  
