<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TODO</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-18mE4kWBq78iYhF1dvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="annonymous">
    <script src="https://kit.fontawesome.com/eb2cfeef2f.js" crossorigin="anonymous"></script>
</head>
<body class="bg-primary">
   <form action="insert.php" method="POST">
        <div class="container">
            <div class="row justify-content-center  m-auto shadow bg-white mt-3 py-3 col-md-6">
                <h3 class="text-center text-primary font-monospace">TODO </h3>
                <div class="col-8">
                     <input type="text" required name="list " class="form-control">
                </div>
                 <div class="col-2">
                    <button class="btn btn-outline-primary"><i class="fa-solid fa-square-plus"></i></button>
                </div>
            </div>
        </div>
    </form>

<!--getdata-->
<?php
include "config.php";
$rawData= mysqli_query($con, "select * from tbltodo");

?>

<div class="container">
     <div class="col-8 bg_white m-auto mt-3">


 <table class="table">
    <tbody>
        <?php
        while($row = mysqli_fetch_array($rawData)){
        
        ?>
        <tr>
           <td><?php echo $row['Id']></td>
           <td><?php echo $row['list']></td>
           <td style="width: 10%;"><a href="delete.php? ID=<?php echo $row['Id']>" class="btn btn-outline-danger"><i class="fa-solid fa-delete-left"></i></a></td>
           <td style="width: 10%;"><a href="update.php? ID=<?php echo $row['Id']>" class="btn btn-outline-success"><i class="fa-solid fa-pen-to-square"></i></a></td>
        </tr>
        <?php
        }
        ?>
    </tbody>
 </table>
</div>
</body>
</html>
