name: Deploy to EC2

on:
  push:
    branches: [ "main" ]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Setup SSH key
      run: |
        mkdir -p ~/.ssh
        echo "${{ secrets.EC2_KEY }}" > ~/.ssh/id_rsa
        chmod 600 ~/.ssh/id_rsa
        ssh-keyscan -H ${{ secrets.EC2_HOST }} >> ~/.ssh/known_hosts

    - name: Deploy on EC2
      run: |
        ssh ${{ secrets.EC2_USER }}@${{ secrets.EC2_HOST }} << 'EOF'
          cd ~/mygitdemo

          # Reset and pull latest code
          git reset --hard
          git pull origin main

          # Install Python + dependencies
          sudo apt-get update -y
          sudo apt-get install -y python3 python3-pip
          pip3 install --upgrade pip
          pip3 install -r requirements.txt

          # Kill old process if running
          pkill -f "python3 app.py" || true

          # Run app in background
          nohup python3 app.py > app.log 2>&1 &
        EOF
