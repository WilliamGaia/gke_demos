# gke_demos
## Walk-through
1. Create a Google Cloud Armor policy *(check [Configuring Google Cloud Armor security policies](https://cloud.google.com/armor/docs/configure-security-policies)
  guide)*.

2. Replace spec.default:
    securityPolicy:`"juice-ca-policy"` variable in `deploy.yaml` file with your Google CloudArmor policy name <YOUR_POLICY_NAME>.
   
3. Apply `deploy.yaml` file
   ```bash
   $ kubectl apply -f deploy.yaml
   deployment.apps/juice-shop created
   service/juice-shop-service created
   backendconfig.cloud.google.com/juice-backendconfig created
   ingress.networking.k8s.io/juice-shop-ingress created
   ```

4. Wait until all created objects reach desired state
   
## Cleanup
```bash
kubectl delete -f deploy.yaml
```
