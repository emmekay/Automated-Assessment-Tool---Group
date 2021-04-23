<?php /*
$username = "root";
$password = "";
$host = "localhost";
$connector = mysql_connect('http://127.0.0.1:5000/', 'c2101138', 'Password123')
    or die("Unable to connect");
$selected = mysql_("survey", $connector)
    or die("Unable to connect");
?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
    <title>Home</title>
    <link href="style/index-layout.css" rel="stylesheet" type="text/css" />
    <link href="style/homepage-layout.css" rel="stylesheet" type="text/css" />
</head>

<body>
    <!--right-->
    <div id="body">
        <div id="left">
        </div>
    </div>
    <?php
    //execute the SQL query and return records
    $result = mysql_query("SELECT * FROM alte_brand");
    ?>
    <table>
        <thead>
            <tr>
                <th>Employee_id</th>
                <th>Employee_Name</th>

            </tr>
        </thead>
        <tbody>
            <?php
            while ($row = mysql_fetch_assoc($result)) {
                echo
                "<tr>
          <td>{$row['bid']}</td>
          <td>{$row['bname']}</td>
        </tr>";
            }
            ?>
        </tbody>
    </table>
</body>

</html>
<?php mysql_close($connector); ?> */