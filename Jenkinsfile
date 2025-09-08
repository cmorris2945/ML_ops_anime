pipeline {
    agent any

     environment{
        VENV_DIR = 'venv'
        GCP_PROJECT = 'gen-lang-client-0315257234'
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
        KUBECTL_AUTH_PLUGIN = "usr/lib/google-cloud-sdk/bin"

     }

    stages{
        stage("Cloning from Githib 'jackass'"){
            steps{
                script{
                    echo 'Cloning from Github Jackass'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'japanese-anime-token', url: 'https://github.com/cmorris2945/ML_ops_anime.git']])
                }

            }
        }

        stage("Now makeing virtual environment..."){
            steps{
                script{
                    echo 'Now makeing virtual environment...'
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    pip install dvc


                    '''
                }

            }
        }

        stage('DVC Pull'){

            steps{
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                        echo 'DVC Pul...'
                        sh'''
                        . ${VENV_DIR}/bin/activate
                        dvc pull



                        '''
                    }

                }
            }
        }

        stage('Build and push image to GCR'){

            steps{
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                        echo 'Build and push image to GCR.'
                        sh'''
                        export PATH=$PATH:${GCLOUD_PATH}
                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                        gcloud config set project ${GCP_PROJECT}
                        gcloud auth configure-docker --quiet
                        docker build -t gcr.io/${GCP_PROJECT}/ml-project:latest .
                        docker push gcr.io/${GCP_PROJECT}/ml-project:latest
                        '''
                    }

                }
            }
        }

    }
}