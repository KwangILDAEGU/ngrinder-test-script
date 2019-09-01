# ngrinder-udp-test-script

nGrinder에서 테스트를 위해 필요한 스크립트 모음 저장소

### 1. How To Use ###
* *UDP 테스트*
    * 필수 정보 수정하기 (socket/udp-client.groovy)
        * 포트 정보 수정 
            ``` python
            port = 7899;
            ```
        * UDP로 전송할 데이터 수정
            ``` python
            def data = "insert data".getBytes();
            ```
            
    
* *MySQL 접속 후, 쿼리 테스트 스크립트 (Database/mysql-query)*
    * 필수 정보 수정하기
        * 필수 변수 수정
            ``` python
            DB_SERVER_IP = "<>:3306" ## Database IP
            DATABASE	 = ""        ## Database Name
            DB_connect = "jdbc:mysql://" + DB_SERVER_IP + "/" + DATABASE
            DB_user = "root"        ## Database User ID
            DB_password = ""        ## Database User Password
            ```

        * 테스트할 쿼리 수정하기
            ``` python
            connection = getConnection()
            selectStatement = connection.createStatement()
            selectStatement.execute("SELECT * FROM table") ## Add Query
            ```