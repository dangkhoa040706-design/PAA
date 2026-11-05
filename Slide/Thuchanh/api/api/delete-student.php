<?php
require_once ('connection.php');

if (!isset($_POST['id']) ) {
    die(json_encode(array('status' => false, 'message' => 'Parameters not valid')));
}

$id = $_POST['id'];

$sql = 'DELETE FROM student where id = ?';


try{
    $stmt = $dbCon->prepare($sql);
    $stmt->execute(array($id));

    $count = $stmt->rowCount();

    if ($count == 1) {
        echo json_encode(array('status' => true, 'message' => 'Xóa sinh viên thành công'));
    }else {
        die(json_encode(array('status' => false, 'message' => 'Mã sinh viên không hợp lệ')));
    }

}
catch(PDOException $ex){
    die(json_encode(array('status' => false, 'message' => $ex->getMessage())));
}



?>
