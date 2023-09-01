<?php

class Order
{
    public $order_number;
    public $order_date;
    public $address;
    public $articles;
}

class Address
{
    public $lastname;
    public $firstname;
    public $street;
    public $postcode;
    public $place;
    public $nation;
    public $company;
}

class Article
{
    public $article_number;
    public $music_sheet;
}

$address = new Address();

$address->lastname = "Steiner";
$address->firstname = "Julian";
$address->street = "Lennesrieth, 16";
$address->postcode = "92727";
$address->place = "Waldthurn";
$address->nation = "DE";
$address->company = "";

$article = new Article();

$article->article_number = "23123124312";
$article->music_sheet = chunk_split(base64_encode(file_get_contents('c:\Users\steinerj\Downloads\The_Pandata_Scalable_Open-Source_Analysis_Stack.pdf')));

$articles = array();
$articles[] = $article;


$order = new Order();

$order->order_number = "BE1234";
$order->order_date = "01.09.2023";
$order->address = $address;
$order->articles = $articles;

$url = "http://127.0.0.1:5000//melicus-musikverlag/order/license";
$data = json_encode($order);

//sending request (according to prosperworks documentation):
// use key 'http' even if you send the request to https://...
$options = array(
    'http' => array(
        'header'  => "Content-Type: application/json\r\n",
        'method'  => 'POST',
        'content' => json_encode($data)
    )
);

$context  = stream_context_create($options);
$result = file_get_contents($url, false, $context);
if ($result === FALSE) { /* Handle error */ }
//compiling to JSON (as wrote above):
$resultData = json_decode($result, TRUE);

foreach ($resultData['data'] as $key => $value) {
    $data = base64_decode($value);
    file_put_contents($key . '.pdf', $data);
}

?>