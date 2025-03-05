pipeline {
    environment {
        IMAGEN = "ivanruiperezb/django_icdc"
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
                stage('Clonar_repo') {
                    steps {
                        git branch:'main',url:'https://github.com/javierasping/django_tutorial_docker.git'
                    }
                }
                stage('Instalar_requeriments') {
                    steps {
                        sh 'pip install -r app/requirements_test.txt'
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
        stage("Generar_imagen") {
            agent any
            stages {
                stage('Construir_imagen') {
                    steps {
                        script {
                            newApp = docker.build "$IMAGEN:latest"
                        }
                    }
                }
                stage('Subir_imagen') {
                    steps {
                        script {
                            docker.withRegistry( '', LOGIN ) {
                                newApp.push()
                            }
                        }
                    }
                }
                stage('Borrar_imagen') {
                    steps {
                        sh "docker rmi $IMAGEN:latest"
                    }
                }
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
