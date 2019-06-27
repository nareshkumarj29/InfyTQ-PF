package main
import ("fmt")
func main(){
    var finalFee int
    var coursefee int=25000
    var marks int=70
    var extrafee int=1500
    finalFee=((coursefee-(marks*coursefee/200))+extrafee)
     fmt.Println(finalFee) 
}
