pipeline {
    environment {
        IMAGEN = "ivanruiperezbe/django_icdc"
        LOGIN = 'DOCKER_HUB_IVANR'
    }
    agent any
    stages {
        stage("Bajar_imagen") {
            agent {
                docker {
                    image "python:3"
                    args '-u root:root'
                }
            }
            stages {
                stage('Repositorio') {
                    steps {
                        git branch:'master',url:'https://github.com/IvanRuiperezB/django_tutorial.git'
                    }
                }
                stage('Requirements') {
                    steps {
                        sh 'pip install -r app/requirements.txt'
                    }
                }
                stage('Test')
                {
                    steps {
                        sh 'cd app && python manage.py test --settings=django_tutorial.desarrollo'
                    }
                }

            }
        }
        stage("Gen_imagen") {
            agent any
            stages {
                stage('build') {
                    steps {
                        script {
                            newApp = docker.build "$IMAGEN:latest"
                        }
                    }
                }
                stage('Subir') {
                    steps {
                        script {
                            docker.withRegistry( '', LOGIN ) {
                                newApp.push()
                            }
                        }
                    }
                }
                stage('Borrar') {
                    steps {
                        sh "docker rmi $IMAGEN:latest"
                    }
                }
            }
        }
    }
    stage('VPS') {
            agent any
            steps {
                sshagent(credentials: ['NEW_KEY']) {
		    sh 'ssh -o StrictHostKeyChecking=no debian@caladan.ivanvan.es docker system prune -f'
                    sh 'ssh -o StrictHostKeyChecking=no javiercruces@atlas.javiercd.es docker image rm -f javierasping/django_tutorial_ic:latest'
                    sh 'ssh -o StrictHostKeyChecking=no javiercruces@atlas.javiercd.es wget https://raw.githubusercontent.com/javierasping/django_tutorial_docker/main/docker-compose.yaml -O docker-compose.yaml'
                    sh 'ssh -o StrictHostKeyChecking=no javiercruces@atlas.javiercd.es docker-compose up -d --force-recreate'
                }
            }
        }
    post {
        always {
            mail to: 'ivanruiperez.instituto@gmail.com',
            subject: "Pipeline IC: ${currentBuild.fullDisplayName}",
            body: "${env.BUILD_URL} has result ${currentBuild.result}"
        }
    }
}
