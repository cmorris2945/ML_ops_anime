pipeline {
    agent any

     environment{
        VENV_DIR = 'venv'
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

    }
}