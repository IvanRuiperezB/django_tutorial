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
                stage('Repositorio') {
                    steps {
                        git branch:'main',url:'https://github.com/IvanRuiperezB/django_tutorial.git'
                    }
                }
                stage('Requirements') {
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
    post {
        always {
            mail to: 'ivanruiperez.instituto@gmail.com',
            subject: "Pipeline IC: ${currentBuild.fullDisplayName}",
            body: "${env.BUILD_URL} has result ${currentBuild.result}"
        }
    }
}
