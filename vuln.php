<?php
if (isset($_GET['file'])) {
    $file = $_GET['file'];
    
    // Allow only the exact traversal path
    if ($file === '../../../../../etc/passwd') {
        header("HTTP/1.1 200 OK"); // Force 200 Response
        echo "<pre>" . file_get_contents('/etc/passwd') . "</pre>";
    } else {
        // Return a 404 response for any other request
        header("HTTP/1.1 404 Not Found");
        echo "404 Not Found";
    }
} else {
    // Return 404 for direct access without 'file' parameter
    header("HTTP/1.1 404 Not Found");
    echo "404 Not Found";
}
?>

