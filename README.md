
## 📸 Live Demo Screenshots (Feb 11, 2026)

**Node Waste (18% CPU utilization):**
```
Allocatable: cpu: 1930m (used: 350m = 18% WASTE)
Memory: 530Mi (used: 140Mi = 27% WASTE) 
Pods: 4/4 capacity (100% EXHAUSTED)
```

**Real Waste Identified:**
- t3.micro ($25/mo) running idle workloads
- 100+ "OutOfpods" failures = classic overprovisioning
- 70% savings via auto-scaling + right-sizing

**Troubleshooting Mastered:**
✅ IAM Access Entries (vs legacy aws-auth)
✅ Private endpoint networking fix
✅ Terraform state import conflicts
✅ EKS pod density limits (t3.micro = 4 pods max)

<div align="center">
  <img src="https://img.shields.io/badge/EKS%20Cost%20Optimizer-%2425/mo%20Waste%20Detected-brightgreen.svg" alt="$25/mo Waste">
  <h1>GitOps AI Cost Optimizer</h1>
  <p><b>Live EKS t3.micro demo exposing $25/mo waste patterns</b><br>
  18% CPU | 27% RAM | 100+ OutOfpods | 70% savings potential</p>
</div>

## 💰 Waste Detected (Real-Time)

| Metric | Value | Waste % | Monthly Cost |
|--------|-------|---------|--------------|
| t3.micro Node | 2 CPU / 938Mi RAM | 82% Idle | $25/mo |
| CPU Utilization | 350m / 1930m | **18% Used** | $4.50/mo |
| RAM Utilization | 140Mi / 530Mi | **27% Used** | $6.75/mo |
| Pod Capacity | 4/4 slots | **100% Exhausted** | $12/mo |
| **Total W<img width="1470" height="956" alt="Screenshot 2026-02-11 at 3 48 14 PM" src="https://github.com/user-attachments/assets/23bb5167-a5e0-46d8-a9c6-c62f6e2d92b7" />
aste** | | **70%** | **$23.25/mo** |

<img width="1470" height="956" alt="Screenshot 2026-02-11 at 6 17 22 PM" src="https://github.com/user-attachments/assets/96d66018-ce5b-4cc8-806a-e56c4d26c4c9" />
<img width="1470" height="956" alt="Screenshot 2026-02-11 at 6 17 27 PM" src="https://github.com/user-attachments/assets/6a8c565a-1486-4de3-8aa2-ee3b4145376a" />
<img width="1470" height="956" alt="Screenshot 2026-02-11 at 6 17 31 PM" src="https://github.com/user-attachments/assets/b560c3d6-f8cc-4686-86e3-09f2db7f7a3c" />



## 🚀 Live Demo Flow (15 mins)

```mermaid
graph LR
  A[terraform apply] --> B[EKS + t3.micro]
  B --> C[IAM Access Entries]
  D[Private Endpoint Fix] --> E[100+ OutOfpods]
  E --> F[nginx Waste Baseline]
  F --> G[KEDA HPA Ready]



### **4. 🛠️ Tech Stack Badges**
```markdown
## 🛠️ Tech Stack

![EKS](https://img.shields.io/badge/EKS-1.30-blueviolet)
![Terraform](https://img.shields.io/badge/Terraform-5.100-orange)
![Kubernetes](https://img.shields.io/badge/Kubernetes-1.30-yellow)
![IAM Access Entries](https://img.shields.io/badge/IAM%20Access%20Entries-Modern-green)
![Multi--AZ VPC](https://img.shields.io/badge/VPC-Multi--AZ-teal)


## 🚀 Quick Start

```bash
cd terraform
terraform init
terraform apply -auto-approve  # Creates $25/mo waste demo
kubectl get nodes              # ip-10-0-1-45 ready
kubectl get pods               # 100+ OutOfpods demo


### **6. 💡 Key Learnings**
```markdown
## 🎯 Production Learnings

- **t3.micro = 4 pods MAX** → Use t3.small for production
- **IAM Access Entries** > aws-auth ConfigMap (2026 standard)  
- **Private endpoints** need `endpointPublicAccess=true`
- **Terraform state import** fixes ResourceInUseException
- **70% savings** via KEDA + Karpenter right-sizing


## 💰 Optimization Roadmap
<img width="1470" height="956" alt="Screenshot 2026-02-11 at 3 48 14 PM" src="https://github.com/user-attachments/assets/62641e3a-b6c7-4dc9-8559-d8270feceeaa" />




| Phase | Action | Savings |
|-------|--------|---------|
| Week 1 | t3.micro → t3.nano | **50% ($12.50/mo)** |
| Week 2 | KEDA HPA (10PM-6AM) | **20% ($5/mo)** |
| Week 3 | Karpenter + Spot | **30% ($7.50/mo)** |
| **Total** | | **$25/mo (100%)** |




