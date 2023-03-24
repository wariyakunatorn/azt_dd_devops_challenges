# AZT DevOps Challenges

## Overview
The purpose of this assessment is to evaluate your technical skills and how you approach infrastructure design. You will be asked to set up a CI/CD pipeline that involves repository setup, pipeline configuration, and Docker image creation.

## We expect you to accomplish the following goals:
1. Fork this repository.
2. Set up a Git repository, preferably using [GitHub](https://github.com), [Gitlab](https://about.gitlab.com) or any other `git` to host the source code of the backend and frontend applications.
3. Set up a CI/CD pipeline using any automation tool of your choice. For example, [Jenkins](https://www.jenkins.io), [GitHub Actions](https://docs.github.com/en/actions), [Gitlab CI/CD](https://docs.gitlab.com/ee/ci/) to automate the building, testing, and deployment of the applications.
4. Use any Docker container registry of your choice. For example, [Docker Hub](https://hub.docker.com) to save the container images.
5. Configure the pipeline to trigger automatically when a pull request is merged into the `main` or `master` branches of your repository. Direct commits into `main` or `master` are not allowed.
6. Use configuration-as-code (CaC) principles as much as possible. Authentication secrets like usernames/passwords/tokens should be isolated from the tools you're using.
7. Containerize the backend and frontend applications and push the Docker images to the container registry of your choice.
8. Deploy the containerized applications to a containerized platform of your choice.

# The deliverables for this task are:
1. Containerize [backend application](./apps/backend) a basic Flask backend application and [frontend application](./apps/frontend) a HTML frontend application and deploy them to a containerized platform of your choice.
2. The backend application should provide a REST API endpoint that returns product information.
3. The frontend application should display this product information to the user.
4. If a product with a given ID is not found, the backend application should return an appropriate error message, and the frontend application should display the message "Product not found".
5. If you are familiar with Kubernetes, you can demonstrate your skills and experience by deploying the application to a Kubernetes cluster and meeting the following basic requirements:
- Deploy the backend and frontend as separate containers in the same Kubernetes cluster.
- Use Kubernetes to manage the deployment, scaling, and health of the containers.
- The backend and frontend should communicate via a Kubernetes service or ingress resource.
- The application should be accessible from outside the Kubernetes cluster via a load balancer or ingress controller.
- Use Kubernetes best practices such as using environment variables for configuration and using Kubernetes secrets for sensitive data.

Overall, the candidate should demonstrate their ability to deploy a containerized application to Kubernetes and manage it effectively using Kubernetes features and best practices.

You are allowed to make changes to the code base if you see fit to meet the above requirements. We encourage you to ask any questions or concerns you may have, or if for any reason you can't finish within the given timeline. Good luck!

# Repository of Allianz Technology Thailand
This code repository is the property of Allianz Technology Thailand. It contains proprietary and confidential information and is intended solely for internal use. Unauthorized access, copying, distribution, or use of this code is strictly prohibited.
