<?php

    $conn = new mysqli("localhost", "root", "", "test");

    if($conn->connect_error){
        die("DB error");
    }

    $data = json_decode(file_get_contents("php://input"), true);


    try{
        $name = $data["name"] ?? "";
        $age = $data["age"] ?? 0;
        $address = $data["address"] ?? "";

        $stmt = $conn->prepare("INSERT INTO users(name, age, address), VALUES(?,?,?)");
        $stmt->bind_param("sis", $name, $age, $address);
        $stmt->execute();
        $result = $stmt->get_result();

        if($result->num_rows===1){
            echo json_encode(
                [
                    "status" => "Success",
                    "message" => "user added"
                ]
            );
        }else{
            echo json_encode(
                [
                    "status"=> "Error",
                    "message" => "User unsucessfully added"
                ]
            );
        }



    }catch(ErrorException $error){
        throw new ErrorException("Invalid not added");

        $stmt->close();
    }
   
    $conn->close()

?>