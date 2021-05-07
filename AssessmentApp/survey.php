<?php'''
    $username = "c2101138"; 
    $password = "Password123";   
    $host = "csmysql.cs.cf.ac.uk:3306";
    $database= "c2101138_cmt313";
    
    $server = mysql_connect($host, $username, $password);
    $connection = mysql_select_db($database, $server);

    $myquery = "
SELECT 'assessment_id', 'question_1' FROM 'surveyinput'
";
    $query = mysql_query($myquery);
    
    if ( ! $query ) {
        echo mysql_error();
        die;
    }
    
    $data = array();
    
    for ($x = 0; $x < mysql_num_rows($query); $x++) {
        $data[] = mysql_fetch_assoc($query);
    }
    
    echo json_encode($data);     
     
    mysql_close($server);
'''