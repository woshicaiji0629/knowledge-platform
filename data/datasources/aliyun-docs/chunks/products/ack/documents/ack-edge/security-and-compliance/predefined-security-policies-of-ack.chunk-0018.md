s: 2 selector: matchLabels: app: test-app template: metadata: labels: app: test-app spec: containers: - name: nginx image: nginx:latest ports: - containerPort: 80
