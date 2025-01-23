## Script
````
apiVersion: apps/v1
kind: Deployment
metadata:
  name: script-runner
  labels:
    app: script
spec:
  replicas: 1
  selector:
    matchLabels:
      app: script
  template:
    metadata:
      labels:
        app: script
    spec:
      containers:
      - name: script-container
        image: bash:latest
        command: ["bash", "-c", "while true; do echo 'Running task...'; sleep 5; done"]
````

## Logs
````

        PS C:\docker\Kubernetes\Minikube> kubectl apply -f deploymentscript.yaml
deployment.apps/script-runner created
PS C:\docker\Kubernetes\Minikube> kubectl get pods
NAME                             READY   STATUS      RESTARTS   AGE
job-test-vlrrw                   0/1     Completed   0          5h6m
script-runner-66fcd56f45-lhkt8   1/1     Running     0          11s
web-0                            1/1     Running     0          4h4m
web-1                            1/1     Running     0          4h38m
PS C:\docker\Kubernetes\Minikube> kubectl logs script-runner-66fcd56f45-lhkt8
Running task...
Running task...
Running task...
Running task...
Running task...
Running task...
Running task...
PS C:\docker\Kubernetes\Minikube> kubectl delete -f deploymentscript.yaml
deployment.apps "script-runner" deleted
PS C:\docker\Kubernetes\Minikube> kubectl get pods
NAME                             READY   STATUS        RESTARTS   AGE
job-test-vlrrw                   0/1     Completed     0          5h8m
script-runner-66fcd56f45-lhkt8   1/1     Terminating   0          86s
web-0                            1/1     Running       0          4h5m
web-1                            1/1     Running       0          4h39m
PS C:\docker\Kubernetes\Minikube> kubectl get pods
NAME             READY   STATUS      RESTARTS   AGE
job-test-vlrrw   0/1     Completed   0          5h9m
web-0            1/1     Running     0          4h7m
web-1            1/1     Running     0          4h40m
````
