## Kubernetes: What is it?
Kubernetes is a portable, extensible, open-source platform for managing containerized workloads and services that facilitates
both declarative configuration and automation.

Source: https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/


## Why do I need it?
Containers are a good way to bundle and run your applications. In a production environment, you need to manage the containers
that run the applications and ensure that there is no downtime. For example, if a container goes down, another container needs
to start. Wouldn’t it be easier if this behaviour was handled by a system?

That’s how Kubernetes comes to the rescue! Kubernetes provides you with a framework to run distributed systems resiliently.
It takes care of scaling and failover for your application, provides deployment patterns, and more.


## Introduction to minikube
Minikube is a tool that makes it easy to run Kubernetes locally. Minikube runs a single-node Kubernetes cluster inside a
Virtual Machine (VM) on your laptop for users looking to try out Kubernetes or develop with it day-to-day.

In this example, we’ll use our laptop along with Minikube, VirtualBox and Kubectl to create a single node Kubernetes cluster:
(Source picture:Platform9: https://platform9.com/docs/install-kubernetes-the-ultimate-guide/)

# Overview:

Install VirtualBox on your system:
 
### Minikube install:
On windows, MAC OS or Linux, download and install minikube from the following link:
https://minikube.sigs.k8s.io/docs/start/

Follow the install procedure first and once complete, continue with these steps.

### Start minikube
Minikube gets installed in the ```C:\``` so find the location in file explorer and open up a CMD windows in that directory.

The first install takes a few minutes:

```
C:\minikube>minikube start
C:\minikube>minikube start
* minikube v1.28.0 on Microsoft Windows 11 Home 10.0.22000 Build 22000
* Automatically selected the virtualbox driver
* Downloading VM boot image ...
    > minikube-v1.28.0-amd64.iso....:  65 B / 65 B [---------] 100.00% ? p/s 0s
    > minikube-v1.28.0-amd64.iso:  274.45 MiB / 274.45 MiB  100.00% 7.62 MiB p/
* Starting control plane node minikube in cluster minikube
* Downloading Kubernetes v1.25.3 preload ...
    > preloaded-images-k8s-v18-v1...:  385.44 MiB / 385.44 MiB  100.00% 7.60 Mi
* Creating virtualbox VM (CPUs=2, Memory=6000MB, Disk=20000MB) ...
! This VM is having trouble accessing https://registry.k8s.io
* To pull new external images, you may need to configure a proxy: https://minikube.sigs.k8s.io/docs/reference/networking/proxy/
* Preparing Kubernetes v1.25.3 on Docker 20.10.20 ...
  - Generating certificates and keys ...
  - Booting up control plane ...
  - Configuring RBAC rules ...
  - Using image gcr.io/k8s-minikube/storage-provisioner:v5
* Verifying Kubernetes components...
* Enabled addons: storage-provisioner, default-storageclass
* kubectl not found. If you need it, try: 'minikube kubectl -- get pods -A'
* Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
```

### Kubectl install:
Kubectl is part of the minikube install so you can run kubectl commands just by putting minikube infront of it.

**But** we're going to install kubectl because we want full functionality.

On windows, MAC OS or Linux, download and install kubectl from the following link:
https://kubernetes.io/docs/tasks/tools/install-kubectl/

Find your OS and follow the install process. I ran this command from C:\minikube

```
C:\minikube>curl.exe -LO "https://dl.k8s.io/release/v1.25.0/bin/windows/amd64/kubectl.exe"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   138  100   138    0     0    123      0  0:00:01  0:00:01 --:--:--   423
100 43.6M  100 43.6M    0     0  6420k      0  0:00:06  0:00:06 --:--:-- 7793k
```

### Kubernetes commands
Check kubectl commands work:

```
C:\minikube>kubectl version
WARNING: This version information is deprecated and will be replaced with the output from kubectl version --short.  Use --output=yaml|json to get the full version.
Client Version: version.Info{Major:"1", Minor:"25", GitVersion:"v1.25.0", GitCommit:"a866cbe2e5bbaa01cfd5e969aa3e033f3282a8a2", GitTreeState:"clean", BuildDate:"2022-08-23T17:44:59Z", GoVersion:"go1.19", Compiler:"gc", Platform:"windows/amd64"}
Kustomize Version: v4.5.7
Server Version: version.Info{Major:"1", Minor:"25", GitVersion:"v1.25.3", GitCommit:"434bfd82814af038ad94d62ebe59b133fcb50506", GitTreeState:"clean", BuildDate:"2022-10-12T10:49:09Z", GoVersion:"go1.19.2", Compiler:"gc", Platform:"linux/amd64"}

C:\minikube>kubectl get pods -A
NAMESPACE     NAME                               READY   STATUS    RESTARTS        AGE
kube-system   coredns-565d847f94-5zzq5           1/1     Running   0               7m2s
kube-system   etcd-minikube                      1/1     Running   0               7m15s
kube-system   kube-apiserver-minikube            1/1     Running   0               7m15s
kube-system   kube-controller-manager-minikube   1/1     Running   0               7m15s
kube-system   kube-proxy-zw9qz                   1/1     Running   0               7m2s
kube-system   kube-scheduler-minikube            1/1     Running   0               7m15s
kube-system   storage-provisioner                1/1     Running   1 (6m31s ago)   7m13s
```

The kubectl command creates a deployment and deployments create our pods and keep them up and running. Lets add the meetup-app into minukube:

```
C:\minikube>kubectl create deployment meetup-app --image=dmccuk/meetup-app:first --port=80
deployment.apps/meetup-app created

C:\minikube>kubectl get deployment
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
meetup-app   1/1     1            1           12s

C:\minikube>kubectl get pods
NAME                         READY   STATUS    RESTARTS   AGE
meetup-app-9f6b86b86-l5xm8   1/1     Running   0          21s
```

Lets check out the deployment configuration by checking the yaml file:

```
C:\minikube>kubectl get deployment -o yaml
apiVersion: v1
items:
- apiVersion: apps/v1
  kind: Deployment
  metadata:
    annotations:
      deployment.kubernetes.io/revision: "1"
    creationTimestamp: "2022-11-17T11:51:16Z"
    generation: 1
    labels:
      app: meetup-app
    name: meetup-app
    namespace: default
<results omitted>
```

Now it’s running we can expose it outside of Kubernetes:

```
C:\minikube>kubectl expose deployment meetup-app --type=NodePort
service/meetup-app exposed
```

Other options are available to expose your deployment. These include Port-forwarding, NodePort & Load-balancer.

Once we expose out app, we can check the service. There is our exposed IP address:

```
C:\minikube>kubectl get service
NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP        99m
meetup-app   NodePort    10.97.162.135   <none>        80:30219/TCP   19s
```

### Now get the URL and check it works:

```
C:\minikube>minikube service meetup-app --url
http://192.168.59.100:30219
```

** You can visit the service on in your browser!**

### Let’s scale out application:

```
C:\minikube>kubectl scale deployment meetup-app --replicas=3
deployment.apps/meetup-app scaled
```

And to prove it:

```
C:\minikube>kubectl get po
NAME                         READY   STATUS    RESTARTS   AGE
meetup-app-9f6b86b86-8vxsb   1/1     Running   0          15s
meetup-app-9f6b86b86-l5xm8   1/1     Running   0          3m18s
meetup-app-9f6b86b86-nhfcf   1/1     Running   0          15s
```

We can also get the individual end points:

```
C:\minikube>kubectl get ep meetup-app
NAME         ENDPOINTS                                   AGE
meetup-app   172.17.0.3:80,172.17.0.4:80,172.17.0.5:80   2m13s

C:\minikube>kubectl get po -o wide
NAME                         READY   STATUS    RESTARTS   AGE     IP           NODE       NOMINATED NODE   READINESS GATES
meetup-app-9f6b86b86-8vxsb   1/1     Running   0          45s     172.17.0.4   minikube   <none>           <none>
meetup-app-9f6b86b86-l5xm8   1/1     Running   0          3m48s   172.17.0.3   minikube   <none>           <none>
meetup-app-9f6b86b86-nhfcf   1/1     Running   0          45s     172.17.0.5   minikube   <none>           <none>
```

Testing: If we delete 2 of the pods, what’s going to happen?

```
C:\minikube>kubectl delete po  meetup-app-9f6b86b86-l5xm8 meetup-app-9f6b86b86-nhfcf
pod "meetup-app-9f6b86b86-l5xm8" deleted
pod "meetup-app-9f6b86b86-nhfcf" deleted

C:\minikube>kubectl get po
NAME                         READY   STATUS    RESTARTS   AGE
meetup-app-9f6b86b86-8vxsb   1/1     Running   0          87s
meetup-app-9f6b86b86-mxc8v   1/1     Running   0          11s
meetup-app-9f6b86b86-snn66   1/1     Running   0          11s
```

** They get recreated again!!**

### Now let go to the service URL via minikube:

```
C:\minikube>minikube service meetup-app --url
http://192.168.59.100:30219

C:\minikube>minikube service meetup-app
|-----------|------------|-------------|-----------------------------|
| NAMESPACE |    NAME    | TARGET PORT |             URL             |
|-----------|------------|-------------|-----------------------------|
| default   | meetup-app |          80 | http://192.168.59.100:30219 |
|-----------|------------|-------------|-----------------------------|
* Opening service default/meetup-app in default browser...
 
C:\minikube>kubectl get svc
NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP        103m
meetup-app   NodePort    10.97.162.135   <none>        80:30219/TCP   4m32s

C:\minikube>kubectl describe svc meetup-app
Name:                     meetup-app
Namespace:                default
Labels:                   app=meetup-app
Annotations:              <none>
Selector:                 app=meetup-app
Type:                     NodePort
IP Family Policy:         SingleStack
IP Families:              IPv4
IP:                       10.97.162.135
IPs:                      10.97.162.135
Port:                     <unset>  80/TCP
TargetPort:               80/TCP
NodePort:                 <unset>  30219/TCP
Endpoints:                172.17.0.4:80,172.17.0.5:80,172.17.0.6:80
Session Affinity:         None
External Traffic Policy:  Cluster
Events:                   <none>
```

### Let checkout the dashboard:

```
C:\minikube>minikube dashboard
* Enabling dashboard ...
  - Using image docker.io/kubernetesui/dashboard:v2.7.0
  - Using image docker.io/kubernetesui/metrics-scraper:v1.0.8
* Some dashboard features require the metrics-server addon. To enable all features please run:

        minikube addons enable metrics-server

* Verifying dashboard health ...
* Launching proxy ...
* Verifying proxy health ...
* Opening http://127.0.0.1:56996/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/ in your default browser...
```

**A browser will open and you will see the cluster and information displayed on the webpage. Take a look around.**

Either close the browser or press “Ctrl + c” to close it from the command line. 


## What have you accomplished?

  * Built a docker container for a static website.
  * Pushed your container to the Docker hub
  * Installed and setup minikube and kubectl on you Laptop
  * Started a Kubernetes cluster an ran the container image
  * Exposed the container deployment and port
  * Used minikube to start the container as a Kubernetes service adding replicas
  * Finally started up the Kubernetes dashboard to display information about our cluster and pod.

## Delete deployment and service:

Now that we’ve used Kubernetes to run out container, we can delete the deployment and service.

First, let’s get all the information from Kubernetes that we need to delete it:

```
C:\minikube>kubectl get all
NAME                             READY   STATUS    RESTARTS   AGE
pod/meetup-app-9f6b86b86-8vxsb   1/1     Running   0          5m49s
pod/meetup-app-9f6b86b86-mxc8v   1/1     Running   0          4m33s
pod/meetup-app-9f6b86b86-snn66   1/1     Running   0          4m33s

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP        106m
service/meetup-app   NodePort    10.97.162.135   <none>        80:30219/TCP   7m31s

NAME                         READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/meetup-app   3/3     3            3           8m52s

NAME                                   DESIRED   CURRENT   READY   AGE
replicaset.apps/meetup-app-9f6b86b86   3         3         3       8m52s
```

Now, run this command: geht auch mit kubectl delete service meetup-app, kubectl delete deployment meetup-app

```
C:\minikube>kubectl delete deploy/meetup-app svc/meetup-app
deployment.apps "meetup-app" deleted
service "meetup-app" deleted
```

All that’s left is the minikube cluster.

```
C:\minikube>kubectl get all
NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   107m
```

Lets stop Minikube:

```
C:\minikube>minikube stop
* Stopping node "minikube"  ...
* 1 node stopped.
```

**All done! Great work.**

## minikube start --driver=docker, falls du Kubernetes auf auf Docker als Container starten willst
Das würde Probleme geben da Deployments nicht dort gestartet wurden.
Benutze Befehl minikube update-context
````
C:\docker\Kubernetes\Minikube>minikube update-context 
! Keine Anpassungen erforderlich für den Kontext "minikube" #ich hatte schon update-context ausgeführt
* Der aktuelle Kontext ist "minikube"

C:\docker\Kubernetes\Minikube>kubectl get pods -A
NAMESPACE              NAME                                         READY   STATUS    RESTARTS       AGE
default                meetup-app-f64db594b-96qqh                   1/1     Running   3 (154m ago)   42h
default                meetup-app-f64db594b-cpd9h                   1/1     Running   3 (154m ago)   42h
default                meetup-app-f64db594b-vvhld                   1/1     Running   3 (154m ago)   43h
kube-system            coredns-668d6bf9bc-kwg4f                     1/1     Running   3 (154m ago)   43h
kube-system            etcd-minikube                                1/1     Running   3 (154m ago)   43h
kube-system            kube-apiserver-minikube                      1/1     Running   3 (154m ago)   43h
kube-system            kube-controller-manager-minikube             1/1     Running   3 (154m ago)   43h
kube-system            kube-proxy-ll68w                             1/1     Running   3 (154m ago)   43h
kube-system            kube-scheduler-minikube                      1/1     Running   3 (154m ago)   43h
kube-system            storage-provisioner                          1/1     Running   6 (154m ago)   43h
kubernetes-dashboard   dashboard-metrics-scraper-5d59dccf9b-2thhv   1/1     Running   3 (154m ago)   42h
kubernetes-dashboard   kubernetes-dashboard-7779f9b69b-6456v        1/1     Running   5 (153m ago)   42h

````

## Deployments und andere Funktionen

````
Was ist ein Deployment?

Ein Deployment sorgt dafür, dass eine bestimmte Anzahl von Pod-Replikaten (Replikas) einer Anwendung ausgeführt wird. Es ist ideal, wenn du stateless Anwendungen (z. B. Webserver) bereitstellen möchtest.

Ein Deployment bietet:

    Skalierbarkeit: Du kannst die Anzahl der Pods anpassen.
    Selbstheilung: Kubernetes startet abgestürzte Pods neu.
    Rolling Updates: Nahtlose Aktualisierung deiner Anwendungsversionen.
    Rollback: Möglichkeit, auf eine frühere Version zurückzuwechseln.

Andere Möglichkeiten, Anwendungen bereitzustellen

Neben Deployments gibt es verschiedene Ressourcen in Kubernetes für unterschiedliche Anforderungen:
1. StatefulSet

    Wird verwendet, wenn der Zustand der Anwendung wichtig ist (z. B. Datenbanken, Apache Kafka, Elasticsearch).
    Bietet garantierte Pod-Identitäten (z. B. pod-0, pod-1) und persistente Speicheranbindung.
    Beispiele:
        MySQL, MongoDB, PostgreSQL.

2. DaemonSet

    Gewährleistet, dass ein Pod auf allen Nodes oder einer spezifischen Node-Gruppe im Cluster läuft.
    Ideal für Node-spezifische Dienste wie Logging, Monitoring, oder Netzwerk-Tools.
    Beispiele:
        Fluentd, Prometheus Node Exporter, Cilium.

3. Job

    Führt einmalige Aufgaben aus und endet, sobald sie abgeschlossen sind.
    Beispiele:
        Datenmigration, Batch-Prozesse.

4. CronJob

    Plant wiederkehrende Jobs (ähnlich wie Cron in Linux).
    Beispiele:
        Tägliche Backups, regelmäßige Berichte.

5. ReplicaSet

    Verwaltet die Anzahl der Pod-Replikate, wird jedoch selten direkt verwendet.
    Deployment nutzt intern ein ReplicaSet.

6. Pod

    Die kleinste ausführbare Einheit in Kubernetes.
    Pods werden selten direkt erstellt, da sie keinen automatischen Neustart oder Skalierung unterstützen. Stattdessen werden sie meist über Controller wie Deployments oder StatefulSets verwaltet.

7. Service

    Kein Deployment-Typ, sondern eine Netzwerkressource, die Pods miteinander oder mit der Außenwelt verbindet.
    Arten von Services:
        ClusterIP: Interner Zugriff im Cluster.
        NodePort: Externer Zugriff über einen bestimmten Node-Port.
        LoadBalancer: Externer Zugriff mit integriertem Load-Balancing (Cloud-Umgebungen).

8. Ingress

    Stellt einen HTTP(S)-Load-Balancer bereit, um mehrere Services hinter einer einzigen IP-Adresse zugänglich zu machen.

````
Lets start Multi-node Cluster aber Minikube erlaubt keine direkte Änderung der Cluster-Konfiguration (z. B. Anzahl der Nodes, RAM oder CPU) eines bestehenden Clusters.:

```
C:\minikube>minikube stop
* Stopping node "minikube"  ...
* 1 node stopped.

C:\docker\Kubernetes\Minikube>minikube delete
* "minikube" in docker wird gelöscht...
* Lösche Container "minikube" ...
* C:\Users\farfi\.minikube\machines\minikube wird entfernt...
* Alle Spuren des "minikube" Clusters wurden entfernt.

C:\docker\Kubernetes\Minikube>minikube start --driver=docker --memory=2g --cpus=2 --nodes=3
* minikube v1.35.0 auf Microsoft Windows 11 Home 10.0.22631.4602 Build 22631.4602
* Verwende den Treiber docker basierend auf der Benutzer-Konfiguration
* Verwende den Treiber Docker Desktop mit root-Privilegien
* Starte "minikube" primary control-plane Node im "minikube" Cluster
* Ziehe Base Image v0.0.46 ...
* Erstelle docker container (CPUs=2, Memory=2048MB) ...
! Failing to connect to https://registry.k8s.io/ from inside the minikube container
* Um neue externe Images zu ziehen, müsste eventuell ein Proxy konfiguriert werden: https://minikube.sigs.k8s.io/docs/reference/networking/proxy/
* Vorbereiten von Kubernetes v1.32.0 auf Docker 27.4.1...
  - Generiere Zertifikate und Schlüssel ...
  - Starte Control-Plane ...
  - Konfiguriere RBAC Regeln ...
* Konfiguriere CNI (Container Networking Interface) ...
* Verifiziere Kubernetes Komponenten...
  - Verwende Image gcr.io/k8s-minikube/storage-provisioner:v5
* Addons aktiviert: storage-provisioner, default-storageclass

* Starte "minikube-m02" worker Node im "minikube" Cluster
* Ziehe Base Image v0.0.46 ...
* Erstelle docker container (CPUs=2, Memory=2048MB) ...
* Gefundene Netzwerkoptionen:
  - NO_PROXY=192.168.49.2
  - NO_PROXY=192.168.49.2
! Failing to connect to https://registry.k8s.io/ from inside the minikube container
* Um neue externe Images zu ziehen, müsste eventuell ein Proxy konfiguriert werden: https://minikube.sigs.k8s.io/docs/reference/networking/proxy/
* Vorbereiten von Kubernetes v1.32.0 auf Docker 27.4.1...
  - env NO_PROXY=192.168.49.2
* Verifiziere Kubernetes Komponenten...

* Starte "minikube-m03" worker Node im "minikube" Cluster
* Ziehe Base Image v0.0.46 ...
* Erstelle docker container (CPUs=2, Memory=2048MB) ...
* Gefundene Netzwerkoptionen:
  - NO_PROXY=192.168.49.2,192.168.49.3
  - NO_PROXY=192.168.49.2,192.168.49.3
! Failing to connect to https://registry.k8s.io/ from inside the minikube container
* Um neue externe Images zu ziehen, müsste eventuell ein Proxy konfiguriert werden: https://minikube.sigs.k8s.io/docs/reference/networking/proxy/
* Vorbereiten von Kubernetes v1.32.0 auf Docker 27.4.1...
  - env NO_PROXY=192.168.49.2
  - env NO_PROXY=192.168.49.2,192.168.49.3
* Verifiziere Kubernetes Komponenten...
* kubectl nicht gefunden. Falls Sie es benötigen, versuchen Sie 'minikube kubectl -- get pods -A' aufzurufen
* Fertig! kubectl ist jetzt für die standardmäßige (default) Verwendung des Clusters "minikube" und des Namespaces "default" konfiguriert

```

## kubectl-tools
````
C:\docker\Kubernetes\Minikube>kubectl cluster-info
Kubernetes control plane is running at https://127.0.0.1:60684
CoreDNS is running at https://127.0.0.1:60684/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.

C:\docker\Kubernetes\Minikube>kubectl get nodes
NAME           STATUS   ROLES           AGE     VERSION
minikube       Ready    control-plane   4m17s   v1.32.0
minikube-m02   Ready    <none>          3m31s   v1.32.0
minikube-m03   Ready    <none>          2m42s   v1.32.0

````
##tutorials für andere Ressourcen
````
statefulset
https://kubernetes.io/docs/tutorials/stateful-application/basic-stateful-set/#ordered-pod-creation
job und cronjob
https://opensource.com/article/20/11/kubernetes-jobs-cronjobs
````
