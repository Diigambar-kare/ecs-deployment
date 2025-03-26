# Use the official Jenkins LTS image from Docker Hub
FROM jenkins/jenkins:lts

# Set the working directory inside the container
WORKDIR /app

# Copy your local files into the container's /app directory
COPY . /app

# Expose Jenkins web UI port (default: 8080)
EXPOSE 8080

# Expose the port for JNLP (default: 50000)
EXPOSE 50000

# Run Jenkins as the default user
USER jenkins

# Start Jenkins when the container runs
CMD ["java", "-jar", "/usr/share/jenkins/jenkins.war"]

