#-*- coding: utf-8 -*-
import mock
import unittest
from allegro.lib import downolad_data
from allegro.script import main
from allegro.lib import AllegroError
from bs4 import BeautifulSoup
import mechanize

EXAMPLE_HTML = '''\
<!DOCTYPE html>

<html class="no-js " xmlns="http://www.w3.org/1999/xhtml" xml:lang="pl" lang="pl" xmlns:fb="http://www.facebook.com/2008/fbml" xmlns:og="http://opengraphprotocol.org/schema/">
<head>
<meta charset="utf-8">
   <link rel="shortcut icon" href="http://static.allegrostatic.pl/site_images/1/0/common/favicon2.ico" />
   <link rel="apple-touch-icon" href="http://static.allegrostatic.pl/site_images/1/0/common/icon.jpg"/>

 <title>Laptop - Allegro.pl - Więcej niż aukcje. Najlepsze oferty na największej platformie handlowej.</title>

  <meta name="keywords" content="aukcje internetowe,allegro,serwis aukcyjny" />
 <meta name="description" content="Allegro - najwięcej ofert w jednym miejscu. Radość zakupów i 100% bezpieczeństwa dla każdej transakcji. Kup Teraz!" />
 <meta name="classification" content="global,all" />
 <meta name="robots" content="all,index,follow" />
 <meta name="revisit-after" content="2 days" />


   <meta property="fb:admins" content="1683271640,658737674,638512944" />
  <meta property="fb:page_id" content="169267498107" />





  <link rel="stylesheet" media="screen" type="text/css" href="http://static.allegrostatic.pl/site_images/1/0/css/vela-pages-layout_av.2013.37.4.css" title="" /><link rel="stylesheet" media="print" type="text/css" href="http://static.allegrostatic.pl/site_images/1/0/css/print_av.2013.37.4.css" title="" /><link rel="alternate stylesheet" media="screen" type="text/css" href="http://static.allegrostatic.pl/site_images/1/0/css/print_preview_av.2013.37.4.css" title="Print Preview" /><link rel="stylesheet" media="screen" type="text/css" href="http://c.allegrostatic.pl/styles/vela-common.css?v=88ee4dfc133a763089ddfb1efd87f20c" title="" /><link rel="stylesheet" media="screen" type="text/css" href="http://static.allegrostatic.pl/site_images/1/0/css/vela-layout_av.2013.37.4.css" title="" />

   <link href="https://plus.google.com/100042465934078110473" rel="publisher" />

 <script src="http://static.allegrostatic.pl/js/libs/modernizr-2.6.2.min-3.js"></script>


 <script type="text/javascript" src="//gg.adocean.pl/files/js/ado.js"></script>
 <script type="text/javascript">
 if(typeof ado!=="object"){ado={};ado.config=ado.preview=ado.placement=ado.master=ado.slave=function(){};}
 ado.config({mode: "new", xml: false, characterEncoding: true});
 ado.preview({enabled: true, emiter: "gg.adocean.pl", id: "JOcK7gzdoyrcIT2176iLzhCz8UoPOGcT6Y1ax8FNTPf.l7"});
 ado.master({id: 'OccHlQDANw9IvVa1bbZo9d2Hf7N2rm9aXjdx80etjun.a7', server: 'gg.adocean.pl' });
 </script>


<script type="text/javacript">
// <![CDATA[
 var gomez={
 gs: new Date().getTime(),
 acctId:'B3A70B',
 pgId:'listing',
 grpId:'1',
 wrate:0.01
 };
// ]]>
</script>

<script type="text/javascript">var header=1;</script>
<!-- acmHeader-->

<script type="text/javascript">
 (function() {
 var opti = document.createElement('script'); opti.type = 'text/javascript'; opti.async = true;
 opti.src = '//cdn.optimizely.com/js/70910669.js';
 var s = document.getElementsByTagName('head')[0]; s.appendChild(opti);
 })();
</script>


  <script type="text/javascript">

 var _gaq = _gaq || [];
 var trackers = new Array();


  trackers.push('t0');

 _gaq.push(['t0._setAccount', 'UA-2827377-1']);
   _gaq.push(['t0._setSampleRate', '1']);
    _gaq.push(['t0._setDomainName', '.allegro.pl']);


 _gaq.push(['t0._trackPageview']);




 (function() { var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true; ga.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'stats.g.doubleclick.net/dc.js'; var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s); })();

  </script>

</head>

<!--[if lte IE 8]><body class="ie8 allegro-pl       " data-country-code="1"><![endif]-->
<!--[if gt IE 8]><!--><body class="allegro-pl       " data-country-code="1"><!--<![endif]-->

<!-- Google Tag Manager -->
<noscript><iframe src="//www.googletagmanager.com/ns.html?id=GTM-FXVJ"
 height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
 new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
 j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
 '//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-FXVJ');</script>
<!-- End Google Tag Manager -->


 <input type="hidden" id="cookie-policy-banner-config" data-config='{"url":"http://allegro.pl/country_pages/1/0/cookie_policy.php","langs":{"message":"Strona korzysta z plików cookies w celu realizacji usług i zgodnie z %link%. Możesz określić warunki przechowywania lub dostępu do plików cookies w Twojej przeglądarce.","anchor":"Polityką Plików Cookies"}}'>






<div id="wrapper">
 <div class="vela">
 <!-- MAIN HEADER -->
 <div class="main-header clearfix" id="main-header">

 <!-- USER NAV -->
 <ul class="user-nav">

 <li class="ma-layer">
 <a class="alle-link" href="http://allegro.pl/myaccount/">
 <span>moje allegro</span>
 <i></i>
 </a>
  <ul id="ma-layer">
  <li>
 <a href="http://allegro.pl/myaccount/won.php">
 <span>kupione</span>
 </a>
 </li>
  <li>
 <a href="http://allegro.pl/myaccount/watch.php">
 <span>obserwowane</span>
 </a>
 </li>
  <li>
 <a href="http://allegro.pl/myaccount/bid.php">
 <span>licytujesz</span>
 </a>
 </li>
  <li>
 <a href="http://allegro.pl/NewItem/">
 <span>wystaw przedmiot</span>
 </a>
 </li>
  <li>
 <a href="http://allegro.pl/myaccount/sell.php">
 <span>sprzedajesz</span>
 </a>
 </li>
  <li>
 <a href="http://allegro.pl/myaccount/sold.php">
 <span>sprzedane</span>
 </a>
 </li>
  <li>
 <a href="http://allegro.pl/myaccount/feedbacks/add.php">
 <span>wystaw komentarz</span>
 </a>
 </li>
  <li>
 <a href="http://allegro.pl/myaccount/feedbacks/feedbacks.php">
 <span>komentarze otrzymane</span>
 </a>
 </li>
  </ul>


 <li class="register">
 <a href="http://allegro.pl/Register.php"><span>zarejestruj</span></a>
 </li>

 <li class="login">
 <a href="https://ssl.allegro.pl/fnd/authentication/"><span>zaloguj</span></a>
 </li>


 </ul>
 <!-- / END USER NAV -->


 <!-- SEARCH BAR -->
 <div class="search-bar" id="search-bar">
 <div class="in clearfix">
 <h2 class="logo">
 <a href="http://allegro.pl/" title="Allegro.pl - aukcje internetowe, bezpieczne zakupy">
 <img src="http://static.allegrostatic.pl/site_images/1/0/vela/allegro-logo.png" alt="Allegro.pl - aukcje internetowe, bezpieczne zakupy" width="174" height="59">
 </a>
 </h2>

  <div class="common">
 <form action="http://allegro.pl/listing.php/search" method="get" class="main-search" id="main-search"
 data-actions='{"default":{"action":"\/listing.php\/search","param":"string"},"shop":{"action":"\/shop.php\/Listing","param":"shopName"},"user":{"action":"\/show_user.php","param":"search"},"shopItems":{"action":"\/shop.php\/Show","param":"string"},"userItems":{"action":"\/listing\/user.php","param":"string"}}'
 data-base-url='http://allegro.pl' data-cookie-domain=''>

 <div class="input-text-wrapper">
 <input id="main-search-text" placeholder="czego szukasz?"
 type="text" required="required" name="string"
 value="laptop" x-webkit-speech autocomplete="off">
 </div>

  <select name="search_scope" class="search-type-select">
 <option value="">wszystkie działy</option>
  <option value="electronics">
 Elektronika </option>
  <option value="fashion.beauty">
 Moda i uroda </option>
  <option value="household.health">
 Dom i zdrowie </option>
  <option value="baby">
 Dziecko </option>
  <option value="culture.entertainment">
 Kultura i rozrywka </option>
  <option value="sports.leisure">
 Sport i wypoczynek </option>
  <option value="automotive">
 Motoryzacja </option>
  <option value="collections.art">
 Kolekcje i sztuka </option>
  <option value="company.services">
 Firma i usługi </option>


  <option value="shop">
 sklepy </option>
  <option value="user">
 użytkownicy </option>
  <option value="closed">
 zakończone </option>
  <option class="custom-search-type"></option>
 </select>

 <input type="submit" class="sprite search-btn" value="Szukaj">

  <div class="search-type-select">
 <ul>
 <li><a class="active" href="#">wszystkie działy</a></li>
  <li><a href="#electronics">Elektronika</a></li>
  <li><a href="#fashion.beauty">Moda i uroda</a></li>
  <li><a href="#household.health">Dom i zdrowie</a></li>
  <li><a href="#baby">Dziecko</a></li>
  <li><a href="#culture.entertainment">Kultura i rozrywka</a></li>
  <li><a href="#sports.leisure">Sport i wypoczynek</a></li>
  <li><a href="#automotive">Motoryzacja</a></li>
  <li><a href="#collections.art">Kolekcje i sztuka</a></li>
  <li><a href="#company.services">Firma i usługi</a></li>


  <li class="separator-top">
 <a href="#shop">sklepy</a>
 </li>
  <li>
 <a href="#user">użytkownicy</a>
 </li>
  <li>
 <a href="#closed">zakończone</a>
 </li>
  </ul>
 <strong title="">
  <span>wszystkie działy</span>
  <i class="sprite"></i>
 </strong>
 </div>

 <div class="search-layer">
 <div class="auto-complete-list"></div>
 <label class="in-description">
 <input tabindex="2" type="checkbox" value="1" name="description"> Szukaj też w opisach i parametrach </label>
 </div>

 <script type="text/template" id="default-suggestion-tpl">
 <li data-type="1">
 <span class="phrase"><%= phrase %></span>
 </li>
 </script>

 <script type="text/template" id="in-category-suggestion-tpl">
 <li data-type="2" data-category="<%= category_id %>">
 <span class="phrase"><%= phrase %></span>
 <em>w kategorii <b><%= category %></b></em>
 </li>
 </script>

 <script type="text/template" id="in-history-suggestion-tpl">

 <li data-type="1">
 <a class="remove" href="#" data-id="<%= id %>"><span>usuń</span></a><span class="phrase"><%= phrase %></span>
 </li>

 </script>

 </form>
 </div>

  <div class="cart-status empty">
 <p class="price">
  koszyk jest pusty  </p>
 <p class="count">
 <a href="http://allegro.pl/Cart.php" class="sprite">
 <span></span>
 </a>
 </p>
 </div>
 <a class="toggle-trigger" href="#toggle-trigger" data-lang="">
 <i class="sprite"></i><span class="sprite"></span>
 </a>
  </div>
     </div>
 <!-- /END SEARCH BAR -->

 </div>
 <!-- /END MAIN HEADER -->

 <!-- DEPARTMENTS -->
  <div class="main-nav clearfix" id="main-nav" data-url-root="http://allegro.pl/dzial/layer">
    <ul>
                        <li class="nav-tab">
        <a class="nav-link" href="http://allegro.pl/dzial/elektronika">
            <strong>Elektronika</strong>
        </a>
        <div class="layer-wrapper">
            <div class="layer" data-department="electronics"></div>
        </div>
    </li>

                        <li class="nav-tab">
        <a class="nav-link" href="http://allegro.pl/dzial/moda-i-uroda">
            <strong>Moda <span>i uroda</span></strong>
        </a>
        <div class="layer-wrapper">
            <div class="layer" data-department="fashion.beauty"></div>
        </div>
    </li>

                        <li class="nav-tab">
        <a class="nav-link" href="http://allegro.pl/dzial/dom-i-zdrowie">
            <strong>Dom <span>i zdrowie</span></strong>
        </a>
        <div class="layer-wrapper">
            <div class="layer" data-department="household.health"></div>
        </div>
    </li>

                        <li class="nav-tab">
        <a class="nav-link" href="http://allegro.pl/dzial/dziecko">
            <strong>Dziecko</strong>
        </a>
        <div class="layer-wrapper">
            <div class="layer" data-department="baby"></div>
        </div>
    </li>

                        <li class="nav-tab">
        <a class="nav-link" href="http://allegro.pl/dzial/kultura-i-rozrywka">
            <strong>Kultura <span>i rozrywka</span></strong>
        </a>
        <div class="layer-wrapper">
            <div class="layer" data-department="culture.entertainment"></div>
        </div>
    </li>

                        <li class="nav-tab">
        <a class="nav-link" href="http://allegro.pl/dzial/sport-i-wypoczynek">
            <strong>Sport <span>i wypoczynek</span></strong>
        </a>
        <div class="layer-wrapper">
            <div class="layer" data-department="sports.leisure"></div>
        </div>
    </li>

                        <li class="nav-tab">
        <a class="nav-link" href="http://allegro.pl/dzial/motoryzacja">
            <strong>Motoryzacja</strong>
        </a>
        <div class="layer-wrapper">
            <div class="layer" data-department="automotive"></div>
        </div>
    </li>

                        <li class="nav-tab">
        <a class="nav-link" href="http://allegro.pl/dzial/kolekcje-i-sztuka">
            <strong>Kolekcje <span>i sztuka</span></strong>
        </a>
        <div class="layer-wrapper">
            <div class="layer" data-department="collections.art"></div>
        </div>
    </li>

                        <li class="nav-tab">
        <a class="nav-link" href="http://allegro.pl/dzial/firma-i-uslugi">
            <strong>Firma <span>i usługi</span></strong>
        </a>
        <div class="layer-wrapper">
            <div class="layer" data-department="company.services"></div>
        </div>
    </li>

                    <li class="nav-tab last-child">
        <a class="nav-link" href="http://allegro.pl/dzial/strefa-okazji">
            <strong>Strefa <span>okazji</span></strong>
        </a>
        <div class="layer-wrapper">
            <div class="layer" data-department="other"></div>
        </div>
    </li>

    </ul>
</div>

  <!-- END DEPARTMENTS -->

 <!-- BREADCRUMBS -->
  <div class="main-breadcrumb separator-bottom   search">
 <div class="main-functional-button">
  <div class="btn-group" role="listbox">
  <button class="btn" type="button" role="option" id="add-search-to-favourites" onClick="location.href='/myaccount/favourites/favourites_search.php/addNew/?change_view=Poka%C5%BC&endingTime=7&offerTypeBuyNow=1&standard_allegro=1&string=laptop'">
 dodaj do ulubionych zapytań </button>
  <button class="btn dropdown-toggle" type="button" role="option" data-toggle="dropdown">
 <span class="carret"></span>
 </button>
 <ul class="dropdown-menu menu-to-right" role="option">
  <li><a id="rss-feed-search" href="/rss.php?feed=search&change_view=Poka%C5%BC&endingTime=7&offerTypeBuyNow=1&standard_allegro=1&string=laptop"
 >dodaj kanał RSS </a></li>
  </ul>
  </div>
  </div>
 <div class="main-title-breadcrumbs clearfix">
 <div class="main-title">
 <h1>szukasz <span>laptop</span></h1>
<small id="main-breadcrumb-search-hits">(1359 ofert)</small>
 </div>
  <ul class="main-breadcrumb-list clearfix" id="breadcrumbs-list">
 <li>
 <a href="http://allegro.pl"><span>Allegro</span></a>
 </li>

  <li>Wyniki wyszukiwania</li> </ul>
 </div>
 </div>
  <!-- END BREADCRUMBS -->

</div>


  <div id="pagecontent1" class="main-content clearfix">









 <div id="sidebar" class="sidebar">
 <section class="widget" id="sidebar-categories" data-current-category-id="" data-current-category-name="">
 <div class="widget-header" data-helptip-body='' data-helptip-uri="true"
 >
 <h2>Podkategorie</h2>
    </div>
 <div class="widget-content">
 <nav class="widget-nav">
 <ul>
   <li id="sidebar-cat-2" class="sidebar-cat">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=2&offerTypeBuyNow=1&standard_allegro=1&string=laptop">
 <span class="name"><span>Komputery</span></span>
 </a>
 <span class="count">(1208)</span>
  </li>
  <li id="sidebar-cat-11763" class="sidebar-cat">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=11763&offerTypeBuyNow=1&standard_allegro=1&string=laptop">
 <span class="name"><span>Dla Dzieci</span></span>
 </a>
 <span class="count">(52)</span>
  </li>
  <li id="sidebar-cat-1454" class="sidebar-cat">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=1454&offerTypeBuyNow=1&standard_allegro=1&string=laptop">
 <span class="name"><span>Odzież, Obuwie, Dodatki</span></span>
 </a>
 <span class="count">(45)</span>
  </li>
  <li id="sidebar-cat-3919" class="sidebar-cat">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=3919&offerTypeBuyNow=1&standard_allegro=1&string=laptop">
 <span class="name"><span>Sport i Turystyka</span></span>
 </a>
 <span class="count">(15)</span>
  </li>
  <li id="sidebar-cat-5" class="sidebar-cat">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=5&offerTypeBuyNow=1&standard_allegro=1&string=laptop">
 <span class="name"><span>Dom i Ogród</span></span>
 </a>
 <span class="count">(14)</span>
  </li>
  <li id="sidebar-cat-3" class="sidebar-cat">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=3&offerTypeBuyNow=1&standard_allegro=1&string=laptop">
 <span class="name"><span>Motoryzacja</span></span>
 </a>
 <span class="count">(7)</span>
  </li>
  <li id="sidebar-cat-64477" class="sidebar-cat">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=64477&offerTypeBuyNow=1&standard_allegro=1&string=laptop">
 <span class="name"><span>Biuro i Reklama</span></span>
 </a>
 <span class="count">(7)</span>
  </li>
  <li id="sidebar-cat-122332" class="sidebar-cat">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=122332&offerTypeBuyNow=1&standard_allegro=1&string=laptop">
 <span class="name"><span>Sprzęt estradowy, studyjny i DJ-ski</span></span>
 </a>
 <span class="count">(5)</span>
  </li>
  <li id="sidebar-cat-10" class="sidebar-cat">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=10&offerTypeBuyNow=1&standard_allegro=1&string=laptop">
 <span class="name"><span>RTV i AGD</span></span>
 </a>
 <span class="count">(4)</span>
  </li>
  <li id="sidebar-cat-4" class="sidebar-cat">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=4&offerTypeBuyNow=1&standard_allegro=1&string=laptop">
 <span class="name"><span>Telefony i Akcesoria</span></span>
 </a>
 <span class="count">(1)</span>
  </li>
  <li id="sidebar-cat-122640" class="sidebar-cat">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=122640&offerTypeBuyNow=1&standard_allegro=1&string=laptop">
 <span class="name"><span>Instrumenty</span></span>
 </a>
 <span class="count">(1)</span>
  </li>
  <li id="sidebar-cat-26013" class="sidebar-cat empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=26013&offerTypeBuyNow=1&standard_allegro=1&string=laptop">
 <span class="name"><span>Antyki i Sztuka</span></span>
 </a>
 <span class="count">(0)</span>
  </li>
  <li id="sidebar-cat-98553" class="sidebar-cat empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=98553&offerTypeBuyNow=1&standard_allegro=1&string=laptop">
 <span class="name"><span>Bilety</span></span>
 </a>
 <span class="count">(0)</span>
  </li>
  <li id="sidebar-cat-19732" class="sidebar-cat empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=19732&offerTypeBuyNow=1&standard_allegro=1&string=laptop">
 <span class="name"><span>Biżuteria i Zegarki</span></span>
 </a>
 <span class="count">(0)</span>
  </li>
  <li id="sidebar-cat-73973" class="sidebar-cat empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=73973&offerTypeBuyNow=1&standard_allegro=1&string=laptop">
 <span class="name"><span>Delikatesy</span></span>
 </a>
 <span class="count">(0)</span>
  </li>
  <li id="sidebar-cat-63757" class="sidebar-cat empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=63757&offerTypeBuyNow=1&standard_allegro=1&string=laptop">
 <span class="name"><span>Erotyka</span></span>
 </a>
 <span class="count">(0)</span>
  </li>
  <li id="sidebar-cat-20585" class="sidebar-cat empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=20585&offerTypeBuyNow=1&standard_allegro=1&string=laptop">
 <span class="name"><span>Filmy</span></span>
 </a>
 <span class="count">(0)</span>
  </li>
  <li id="sidebar-cat-8845" class="sidebar-cat empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=8845&offerTypeBuyNow=1&standard_allegro=1&string=laptop">
 <span class="name"><span>Fotografia</span></span>
 </a>
 <span class="count">(0)</span>
  </li>
  <li id="sidebar-cat-9" class="sidebar-cat empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=9&offerTypeBuyNow=1&standard_allegro=1&string=laptop">
 <span class="name"><span>Gry</span></span>
 </a>
 <span class="count">(0)</span>
  </li>
  <li id="sidebar-cat-6" class="sidebar-cat empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=6&offerTypeBuyNow=1&standard_allegro=1&string=laptop">
 <span class="name"><span>Kolekcje</span></span>
 </a>
 <span class="count">(0)</span>
  </li>
  <li id="sidebar-cat-122233" class="sidebar-cat empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=122233&offerTypeBuyNow=1&standard_allegro=1&string=laptop">
 <span class="name"><span>Konsole i automaty</span></span>
 </a>
 <span class="count">(0)</span>
  </li>
  <li id="sidebar-cat-7" class="sidebar-cat empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=7&offerTypeBuyNow=1&standard_allegro=1&string=laptop">
 <span class="name"><span>Książki i Komiksy</span></span>
 </a>
 <span class="count">(0)</span>
  </li>
  <li id="sidebar-cat-1" class="sidebar-cat empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=1&offerTypeBuyNow=1&standard_allegro=1&string=laptop">
 <span class="name"><span>Muzyka</span></span>
 </a>
 <span class="count">(0)</span>
  </li>
  <li id="sidebar-cat-20782" class="sidebar-cat empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=20782&offerTypeBuyNow=1&standard_allegro=1&string=laptop">
 <span class="name"><span>Nieruchomości</span></span>
 </a>
 <span class="count">(0)</span>
  </li>
  <li id="sidebar-cat-16696" class="sidebar-cat empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=16696&offerTypeBuyNow=1&standard_allegro=1&string=laptop">
 <span class="name"><span>Przemysł</span></span>
 </a>
 <span class="count">(0)</span>
  </li>
  <li id="sidebar-cat-76593" class="sidebar-cat empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=76593&offerTypeBuyNow=1&standard_allegro=1&string=laptop">
 <span class="name"><span>Rękodzieło</span></span>
 </a>
 <span class="count">(0)</span>
  </li>
  <li id="sidebar-cat-1429" class="sidebar-cat empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=1429&offerTypeBuyNow=1&standard_allegro=1&string=laptop">
 <span class="name"><span>Uroda</span></span>
 </a>
 <span class="count">(0)</span>
  </li>
  <li id="sidebar-cat-105411" class="sidebar-cat empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=105411&offerTypeBuyNow=1&standard_allegro=1&string=laptop">
 <span class="name"><span>Usługi</span></span>
 </a>
 <span class="count">(0)</span>
  </li>
  <li id="sidebar-cat-55067" class="sidebar-cat empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=55067&offerTypeBuyNow=1&standard_allegro=1&string=laptop">
 <span class="name"><span>Wakacje</span></span>
 </a>
 <span class="count">(0)</span>
  </li>
  <li id="sidebar-cat-121882" class="sidebar-cat empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=121882&offerTypeBuyNow=1&standard_allegro=1&string=laptop">
 <span class="name"><span>Zdrowie</span></span>
 </a>
 <span class="count">(0)</span>
  </li>
   </ul>
 </nav>
 </div>
</section>
 <section id="sidebar-params" class="widget widget-params widget-params-live">
 <div class="widget-header">
 <h2 class="headerBar">Parametry</h2>
 <a class="action action-reset" href="#"><span>Wyczyść</span></a>
 </div>
 <div class="widget-content">
 <input type="hidden" class="jslangs" data-no-param-found="Nie znaleziono parametru." data-search-other="znajdź inne" data-choose="Wybierz" />
 <form action="/listing/listing.php" method="get" name="display-form" id="display-form" data-token="cfab3fa6ddb2ab8147e78b0365bb3213" >
  <input type="hidden" name="string" value="laptop" />


   <fieldset>
 <h3>Stan</h3>
 <ul>
 <li>
 <input name="buyNew" type="checkbox" id="offerBuy4" value="1" />
 <label for="offerBuy4">Nowe <span class="count ">(1302)</span></label>
 </li>
 <li>
 <input name="buyUsed" type="checkbox" id="offerBuy5" value="1" />
 <label for="offerBuy5">Używane <span class="count ">(53)</span></label>
 </li>
 </ul>
 </fieldset>
   <fieldset>
 <h3>Rodzaj oferty</h3>
 <ul>
   <li>
 <input name="offerTypeBuyNow" type="checkbox" id="buyNowParam" value="1" />
 <label for="buyNowParam" class="buyNow">Kup Teraz <span class="count ">(1359)</span></label>
 </li>
       <li>
 <input name="offerTypeAuction" type="checkbox" id="auctionsParam" value="2" />
 <label for="auctionsParam" >Licytacje <span class="count ">(14)</span></label>
 </li>
        </ul>
 </fieldset>

  <fieldset>
 <h3>Cena (zł)</h3>
 <ul class="param-price-range">
 <li class="param-type-range param-type-placeholder">
 <input type="checkbox" value="1" name="price_enabled" />
 <label for="price_from"><span>od</span></label>
 <input type="text" name="price_from" id="price_from" data-validate-anchor="priceFrom" data-error-style="tooltip" placeholder="od" value="" size="5" />&ndash;
 <label for="price_to"><span>do</span></label>
 <input type="text" name="price_to" id="price_to" data-validate-anchor="priceTo" data-error-style="tooltip" placeholder="do" value="" size="5" />
 </li>
 </ul>
 </fieldset>

   <fieldset>
 <h3>Lokalizacja</h3>
 <ul>
 <li class="param-type-placeholder">
 <input id="locationRadio3" type="radio" name="postcode_enabled" value="2" />
 <label for="city_id">miejscowość:</label>
 <input type="text" name="city" id="city_id" size="10" placeholder="miejscowość" value="" />
 </li>
 <li class="param-type-placeholder param-distance-state">
 <input id="locationRadio1" type="radio" name="postcode_enabled" value="0" checked="checked" />
 <select name="state" id="state" placeholder="województwo">
 <option value="" class="disabled">województwo</option>
 <option value="1">z dolnośląskiego</option><option value="2">z kujawsko-pomorskiego</option><option value="3">z lubelskiego</option><option value="4">z lubuskiego</option><option value="5">z łódzkiego</option><option value="6">z małopolskiego</option><option value="7">z mazowieckiego</option><option value="8">z opolskiego</option><option value="9">z podkarpackiego</option><option value="10">z podlaskiego</option><option value="11">z pomorskiego</option><option value="12">ze śląskiego</option><option value="13">ze świętokrzyskiego</option><option value="14">z warmińsko-mazurskiego</option><option value="15">z wielkopolskiego</option><option value="16">z zachodniopomorskiego</option> </select>
 </li>
  <li class="param-type-placeholder param-distance-postcode">
 <input type="radio" id="locationRadio2" name="postcode_enabled" value="1" />
 <label for="postcode_enabled">w odległości do:</label>
 <select name="distance" class="cLabel" placeholder="km" data-dependent='["postcode"]'>
 <option value="" class="disabled">km</option>
 <option value="1">10</option><option value="2">25</option><option value="3">50</option><option value="4">75</option><option value="5">100</option><option value="6">150</option><option value="7">200</option><option value="8">350</option><option value="9">500</option> </select>
 <span>od</span>
 <label for="distanceFromPostcodeInput"><span>kod</span></label>
 <input type="text" name="postcode" id="distanceFromPostcodeInput" size="6" maxlength="6" placeholder="kod" data-dependent='["distance"]' data-validate-anchor="postcode" data-error-style="tooltip"  />
 </li>
  </ul>
 </fieldset>

 <div class="">

 <div id="moreParamsBlock">
  </div>
  </div><!-- /catAttribBlock -->

 <fieldset>
 <h3>oferta ma</h3>
 <ul class="no-scroll">
  <li>
 <input type="checkbox" name="standard_allegro" id="standard_allegro1" value="1" checked="checked" />
 <label for="standard_allegro1">Standard Allegro <i class="icon-as"></i></label>
 </li>
   <li>
 <input id="freeShipping" type="checkbox" name="freeShipping" value="1" />
 <label for="freeShipping">wysyłka GRATIS <i class="icon-fs"></i></label>
 </li>
    <li>
 <input id="installmentAvailable" type="checkbox" name="installmentAvailable" value="1" data-helptip-body="Dodaliśmy filtr <em>Raty PayU</em>. Zaznacz go, jeśli chcesz zobaczyć tylko oferty, za które możesz zapłacić w ratach." >
 <label for="installmentAvailable">Raty <span class="specialcase">PayU</span> <i class="icon-pi"></i></label>
 </li>

  <li>
 <input id="personal_id" type="checkbox" name="personal_rec" value="1" />
 <label for="personal_id">Odbiór osobisty</label>
 </li>


  <li>
 <input id="vat_id" type="checkbox" name="vat_invoice" value="1" />
 <label for="vat_id">Faktura <span class="specialcase">VAT</span> <!-- <span class="count">()</span> --></label>
 </li>

  <li>
 <input id="generalDelivery_id" type="checkbox" name="generalDelivery_rec" value="1" />
 <label for="generalDelivery_id">Odbiór w punkcie</label>
 </li>

   </ul>
 </fieldset>

   <fieldset>
 <h3>Czas realizacji</h3>
 <ul>
 <li class="param-type-placeholder param-shipping-time">
 <input type="checkbox" name="shippingTime_enabled" value="1" />
 <select id="shippingTime" name="shippingTime" placeholder="czas">
 <option value="" class="disabled">czas</option>
  <option id="shippingTime_24" value="24">24 godziny</option>
  <option id="shippingTime_48" value="48">do 2 dni</option>
  <option id="shippingTime_72" value="72">do 3 dni</option>
  <option id="shippingTime_96" value="96">do 4 dni</option>
  <option id="shippingTime_120" value="120">do 5 dni</option>
  <option id="shippingTime_168" value="168">do 7 dni</option>
  <option id="shippingTime_240" value="240">do 10 dni</option>
  <option id="shippingTime_336" value="336">do 14 dni</option>
  <option id="shippingTime_504" value="504">do 21 dni</option>
  <option id="shippingTime_999" value="999">dłużej</option>
  </select>
 </li>
 </ul>
 </fieldset>

 <fieldset>
 <h3>wystawione</h3>
 <ul>
 <li class="param-type-placeholder">
 <input type="checkbox" name="startingTime_enabled" value="1" />
 <span>w ciągu</span>
 <select name="startingTime" id="startingTime_id" placeholder="czas">
 <option value="" class="disabled">czas</option>
 <option value="1">1 godziny</option><option value="2">2 godzin</option><option value="3">3 godzin</option><option value="4">4 godzin</option><option value="5">5 godzin</option><option value="6">12 godzin</option><option value="7" selected="selected">24 godzin</option><option value="8">2 dni</option><option value="9">3 dni</option><option value="10">4 dni</option><option value="11">5 dni</option><option value="12">6 dni</option><option value="13">7 dni</option> </select>
 </li>
 </ul>
 </fieldset>

 <fieldset>
 <h3>kończące się</h3>
 <ul>
 <li class="param-type-placeholder">
 <input type="checkbox" name="endingTime_enabled" value="1" />
 <span>w ciągu</span>
 <select name="endingTime" id="endingTime_id" placeholder="czas">
 <option value="" class="disabled">czas</option>
 <option value="1">1 godziny</option><option value="2">2 godzin</option><option value="3">3 godzin</option><option value="4">4 godzin</option><option value="5">5 godzin</option><option value="6">12 godzin</option><option value="7" selected="selected">24 godzin</option><option value="8">2 dni</option><option value="9">3 dni</option><option value="10">4 dni</option><option value="11">5 dni</option><option value="12">6 dni</option><option value="13">7 dni</option> </select>
 </li>
 </ul>
 </fieldset>


 <div class="clearfix"></div>
 <fieldset class="submit">
 <div class="button-wrapper">
 <input type="submit" class="btn" value="Pokaż" name="change_view" />
 </div>
 </fieldset>
  </form>
 </div>
 <script id="sidebar-params-validation-rules" type="js/data">

 {
 "postcode":[{"required":false},{"pattern":"postcodePL","msg":"Niewłaściwy sposób zapisu"},{"minLength":4,"msg":"Zbyt krótki wpis"},{"maxLength":12,"msg":"Zbyt długi wpis"}],
 "priceFrom":[{"required":false},{"pattern":"amountPL","msg":"Niewłaściwy sposób zapisu"}],
 "priceTo":[{"required":false},{"pattern":"amountPL","msg":"Niewłaściwy sposób zapisu"}]
 }

 </script>
 <script id="sidebar-params-validation-samples" type="js/data">
 {"postcode":"00-000"}
 </script>
</section><!-- /sidebar-params -->

<script id="sidebar-params-toggle-link" type="text/template">
 <a href="#" class="toggle expanded">
 <span class="label-collapse"><span class="arrow">&lt;</span> <span>mniej</span></span>
 <span class="label-expand"><span>więcej</span> <span class="arrow">&gt;</span></span>
 </a>
</script>


  <section id="sidebar-ceneo" class="widget widget-adverts widget-ceneo">
 <div class="widget-header">
 <h3><a href="http://www.ceneo.pl" rel="external" target="_blank"><span>Popularne w <strong class="logo">ceneo</strong></span></a></h3>
 </div>
 <div class="widget-content">
 <ul class="adverts">
  <li>
 <a href="http://www.ceneo.pl/17385867" target="_blank">
 <img src="http://staticpics.allegrostatic.pl/public/ceneo/17/1738/173858/17385867.jpg" alt="" class="photo"> <span class="name"><span>HP 655 (B6N21EA)</span></span>
 </a>
 </li>
  <li>
 <a href="http://www.ceneo.pl/19522552" target="_blank">
 <img src="http://staticpics.allegrostatic.pl/public/ceneo/19/1952/195225/19522552.jpg" alt="" class="photo"> <span class="name"><span>Lenovo IdeaPad Y580</span></span>
 </a>
 </li>
  <li>
 <a href="http://www.ceneo.pl/21187151" target="_blank">
 <img src="http://staticpics.allegrostatic.pl/public/ceneo/21/2118/211871/21187151.jpg" alt="" class="photo"> <span class="name"><span>Samsung 550P5C</span></span>
 </a>
 </li>
  </ul>
 </div>
 <div class="widget-footer">
  zobacz <a href="http://www.ceneo.pl/;szukaj-laptop" target="_blank"><span>laptop</span></a> w&nbsp;Ceneo  </div>
 </section>


  <section id="sidebar-adocean" class="widget widget-adverts widget-adocean">
 <div class="widget-content">
 <div data-adocean-id="l_left_top_160_600" style="display: none;"><div id="adoceanggwahqcklrae" data-ad="1"></div></div> <div data-adocean-id="l_left_bottom_160_600" style="display: none;"><div id="adoceanggtboggxegud" data-ad="1"></div></div> </div>
 </section>
 </div>
<div id="listing" class="listing " data-is-live-search-active="1" data-popup='{"token":"cfab3fa6ddb2ab8147e78b0365bb3213","cartid":""}' data-txt='{"samplePhoto":"zdjęcie poglądowe","loading":"Ładowanie"}' data-catcounters='{"2":1208,"11763":52,"1454":45,"3919":15,"5":14,"3":7,"64477":7,"122332":5,"10":4,"4":1,"122640":1,"26013":0,"98553":0,"19732":0,"73973":0,"63757":0,"20585":0,"8845":0,"9":0,"6":0,"122233":0,"7":0,"1":0,"20782":0,"16696":0,"76593":0,"1429":0,"105411":0,"55067":0,"121882":0}' data-totalcounter='1359 ofert'  data-headtitle="Laptop - Allegro.pl - Więcej niż aukcje. Najlepsze oferty na największej platformie handlowej.">

 <div class="listing-options">
 <div class="listing-views">
 <a class="view-option view-simple" data-view="listing-simple" title="Widok prosty" href="#">Widok prosty</a>
 <a class="view-option view-normal" data-view="listing-normal" title="Widok szczegółowy" href="#">Widok szczegółowy</a>
 <a class="view-option view-gallery" data-view="listing-gallery" title="Widok galerii" href="#">Widok galerii</a>
 </div>
 <div id="pager-top" class="pager pager-top" rel="23">
 <ul class="pager-nav">
 <li class="prev hidden"><a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&offerTypeBuyNow=1&p=0&standard_allegro=1&string=laptop"><span class="arrow">&lt;</span></a></li>
 <li class="current"><input id="pager-value" type="text" value="1" rel="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&offerTypeBuyNow=1&standard_allegro=1&string=laptop&"/>
 </li>
 <li class="suffix"><span>z</span></li>
 <li><a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&offerTypeBuyNow=1&p=23&standard_allegro=1&string=laptop"><span>23</span></a></li>
 <li class="next"><a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&offerTypeBuyNow=1&p=2&standard_allegro=1&string=laptop"><span class="arrow">&gt;</span></a></li>
 </ul>
</div>

  <div class="listing-sort-dropdown">
 <div class="toggle">
 <span class="label">czas do końca: <strong>najmniej</strong><span class="arrow"></span></span>
 </div>
 <div class="options">
 <dl><dt>cena</dt><dd data-order="p"><a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&offerTypeBuyNow=1&order=p&standard_allegro=1&string=laptop"><span>od najniższej</span></a></dd><dd data-order="pd"><a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&offerTypeBuyNow=1&order=pd&standard_allegro=1&string=laptop"><span>od najwyższej</span></a></dd><dt>cena z dostawą</dt><dd data-order="d"><a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&offerTypeBuyNow=1&order=d&standard_allegro=1&string=laptop"><span>od najniższej</span></a></dd><dd data-order="dd"><a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&offerTypeBuyNow=1&order=dd&standard_allegro=1&string=laptop"><span>od najwyższej</span></a></dd><dt>popularność</dt><dd data-order="qd"><a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&offerTypeBuyNow=1&order=qd&standard_allegro=1&string=laptop"><span>największa</span></a></dd><dd data-order="q"><a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&offerTypeBuyNow=1&order=q&standard_allegro=1&string=laptop"><span>najmniejsza</span></a></dd><dt>czas do końca</dt><dd data-order="t" class="selected"><a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&offerTypeBuyNow=1&order=t&standard_allegro=1&string=laptop"><span>najmniej</span></a></dd><dd data-order="td"><a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&offerTypeBuyNow=1&order=td&standard_allegro=1&string=laptop"><span>najwięcej</span></a></dd><dt>nazwa</dt><dd data-order="n"><a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&offerTypeBuyNow=1&order=n&standard_allegro=1&string=laptop"><span>od A do Z</span></a></dd><dd data-order="nd"><a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&offerTypeBuyNow=1&order=nd&standard_allegro=1&string=laptop"><span>od Z do A</span></a></dd></dl> </div>
 </div>
 </div>

 <section class="offers">
 <h2 class="listing-header">lista promowanych ofert</h2>
 <article id="item-3332485440" class="offer" data-id="3332485440">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/48/54/3332485440","http://img13.allegroimg.pl/photos/128x96/33/32/48/54/3332485440","http://img13.allegroimg.pl/photos/400x300/33/32/48/54/3332485440"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77922","s":"11339433","1234":"2","4326":"7","4327":"32","4329":"2","4346":"7383296","4366":"20","4474":"100","11323":"1"}' >
 <a href="/laptop-samsung-i5-3210m-gt650-8gb-1000gb-windows-8-i3332485440.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 2 739,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 2 739,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332485440/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332485440" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-samsung-i5-3210m-gt650-8gb-1000gb-windows-8-i3332485440.html"><span>LAPTOP Samsung i5-3210M GT650 8GB 1000GB WINDOWS 8</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">3 minuty</strong> Do końca </div>
 <div class="popularity">
    <strong>kupiono  1,
 </strong>
  dostępnych  48 sztuk     </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=LAPTOP Samsung i5-3210M GT650 8GB 1000GB WINDOWS 8&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332485933" class="offer" data-id="3332485933">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/48/59/3332485933","http://img13.allegroimg.pl/photos/128x96/33/32/48/59/3332485933","http://img13.allegroimg.pl/photos/400x300/33/32/48/59/3332485933"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77920","s":"11339433","1234":"2","4326":"3","4327":"16","4329":"2","4346":"35072","4366":"30","4474":"60","11323":"1"}' >
 <a href="/laptop-lenovo-ideapad-s300-stalowy-2-core-hd4000-i3332485933.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 1 389,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 1 389,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332485933/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332485933" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-lenovo-ideapad-s300-stalowy-2-core-hd4000-i3332485933.html"><span>Laptop Lenovo IdeaPad S300 Stalowy 2-core HD4000</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">3 minuty</strong> Do końca </div>
 <div class="popularity">
    <strong>kupiono  2,
 </strong>
  dostępnych  47 sztuk     </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop Lenovo IdeaPad S300 Stalowy 2-core HD4000&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3331544561" class="offer" data-id="3331544561">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img19.allegroimg.pl/photos/64x48/33/31/54/45/3331544561","http://img19.allegroimg.pl/photos/128x96/33/31/54/45/3331544561","http://img19.allegroimg.pl/photos/400x300/33/31/54/45/3331544561"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"85034","s":"15737359","11323":"1"}' >
 <a href="/bk220-wiatrak-wentylator-na-usb-do-pc-laptop-i3331544561.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 14,99 <span class="currency">zł</span> </span>
    <span class="delivery">
  <span class="label">z dostawą</span> 22,99 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3331544561/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3331544561" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/bk220-wiatrak-wentylator-na-usb-do-pc-laptop-i3331544561.html"><span>bk220 WIATRAK WENTYLATOR na USB do PC LAPTOP</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">8 minut</strong> Do końca </div>
 <div class="popularity">
    <strong>kupiono  7,
 </strong>
  dostępne  93 sztuki     </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=bk220 WIATRAK WENTYLATOR na USB do PC LAPTOP&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332513214" class="offer" data-id="3332513214">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img08.allegroimg.pl/photos/64x48/33/32/51/32/3332513214","http://img08.allegroimg.pl/photos/128x96/33/32/51/32/3332513214","http://img08.allegroimg.pl/photos/400x300/33/32/51/32/3332513214"],["http://img08.allegroimg.pl/photos/64x48/33/32/51/32/3332513214_1","http://img08.allegroimg.pl/photos/128x96/33/32/51/32/3332513214_1","http://img08.allegroimg.pl/photos/400x300/33/32/51/32/3332513214_1"],["http://img08.allegroimg.pl/photos/64x48/33/32/51/32/3332513214_2","http://img08.allegroimg.pl/photos/128x96/33/32/51/32/3332513214_2","http://img08.allegroimg.pl/photos/400x300/33/32/51/32/3332513214_2"],["http://img08.allegroimg.pl/photos/64x48/33/32/51/32/3332513214_3","http://img08.allegroimg.pl/photos/128x96/33/32/51/32/3332513214_3","http://img08.allegroimg.pl/photos/400x300/33/32/51/32/3332513214_3"],["http://img08.allegroimg.pl/photos/64x48/33/32/51/32/3332513214_4","http://img08.allegroimg.pl/photos/128x96/33/32/51/32/3332513214_4","http://img08.allegroimg.pl/photos/400x300/33/32/51/32/3332513214_4"],["http://img08.allegroimg.pl/photos/64x48/33/32/51/32/3332513214_5","http://img08.allegroimg.pl/photos/128x96/33/32/51/32/3332513214_5","http://img08.allegroimg.pl/photos/400x300/33/32/51/32/3332513214_5"],["http://img08.allegroimg.pl/photos/64x48/33/32/51/32/3332513214_6","http://img08.allegroimg.pl/photos/128x96/33/32/51/32/3332513214_6","http://img08.allegroimg.pl/photos/400x300/33/32/51/32/3332513214_6"],["http://img08.allegroimg.pl/photos/64x48/33/32/51/32/3332513214_7","http://img08.allegroimg.pl/photos/128x96/33/32/51/32/3332513214_7","http://img08.allegroimg.pl/photos/400x300/33/32/51/32/3332513214_7"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77783","s":"18510999","11323":"1"}' >
 <a href="/plecak-na-laptopa-dell-adventure-17-460-11739-i3332513214.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 159,00 <span class="currency">zł</span> </span>
    <span class="delivery">
  <span class="label">z dostawą</span> 169,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332513214/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332513214" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/plecak-na-laptopa-dell-adventure-17-460-11739-i3332513214.html"><span>plecak na laptopa Dell Adventure 17&#039;&#039; 460-11739</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">11 minut</strong> Do końca </div>
 <div class="popularity">
    <strong>kupiono  5,
 </strong>
  dostępnych  5 sztuk     </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=plecak na laptopa Dell Adventure 17&#039;&#039; 460-11739&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332508142" class="offer" data-id="3332508142">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img03.allegroimg.pl/photos/64x48/33/32/50/81/3332508142","http://img03.allegroimg.pl/photos/128x96/33/32/50/81/3332508142","http://img03.allegroimg.pl/photos/400x300/33/32/50/81/3332508142"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77777","s":"14691954","11323":"1","18469":"2"}' >
 <a href="/ak25a-karta-pcmcia-laptop-hub-usb-2-0-2-porty-slim-i3332508142.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 21,90 <span class="currency">zł</span> </span>
    <span class="delivery">
  <span class="label">z dostawą</span> 35,90 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332508142/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332508142" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/ak25a-karta-pcmcia-laptop-hub-usb-2-0-2-porty-slim-i3332508142.html"><span>AK25A KARTA PCMCIA LAPTOP HUB USB 2.0 2 PORTY SLIM</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">11 minut</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  30 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=AK25A KARTA PCMCIA LAPTOP HUB USB 2.0 2 PORTY SLIM&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332528779" class="offer" data-id="3332528779">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img14.allegroimg.pl/photos/64x48/33/32/52/87/3332528779","http://img14.allegroimg.pl/photos/128x96/33/32/52/87/3332528779","http://img14.allegroimg.pl/photos/400x300/33/32/52/87/3332528779"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77919","s":"5008260","1234":"2","1235":"1","4326":"7","4327":"1","4329":"2","4346":"43264","4366":"30","4474":"100","11323":"1"}' >
 <a href="/laptop-hp-4740s-i3-320gb-6gb-dwrw-b6n47ea-torba-i3332528779.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 2 019,00 <span class="currency">zł</span> </span>
    <span class="delivery">
  <span class="label">z dostawą</span> 2 038,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332528779/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332528779" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-hp-4740s-i3-320gb-6gb-dwrw-b6n47ea-torba-i3332528779.html"><span>Laptop Hp 4740s i3 320GB 6GB DWRW B6N47EA + torba</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">17 minut</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  18 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop Hp 4740s i3 320GB 6GB DWRW B6N47EA + torba&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332528871" class="offer" data-id="3332528871">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img14.allegroimg.pl/photos/64x48/33/32/52/88/3332528871","http://img14.allegroimg.pl/photos/128x96/33/32/52/88/3332528871","http://img14.allegroimg.pl/photos/400x300/33/32/52/88/3332528871"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77919","s":"5008260","1234":"2","1235":"1","4326":"7","4327":"1","4329":"2","4346":"43264","4366":"30","4474":"100","11323":"1"}' >
 <a href="/laptop-hp-4740s-i3-320gb-8gb-dwrw-b6n47ea-torba-i3332528871.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 2 069,00 <span class="currency">zł</span> </span>
    <span class="delivery">
  <span class="label">z dostawą</span> 2 088,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332528871/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332528871" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-hp-4740s-i3-320gb-8gb-dwrw-b6n47ea-torba-i3332528871.html"><span>Laptop Hp 4740s i3 320GB 8GB DWRW B6N47EA + torba</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">17 minut</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  18 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop Hp 4740s i3 320GB 8GB DWRW B6N47EA + torba&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332544805" class="offer" data-id="3332544805">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/54/48/3332544805","http://img13.allegroimg.pl/photos/128x96/33/32/54/48/3332544805","http://img13.allegroimg.pl/photos/400x300/33/32/54/48/3332544805"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77919","s":"11339433","1234":"1","4326":"5","4327":"32","4329":"2","4346":"6334720","4366":"30","4474":"60","11323":"1"}' >
 <a href="/laptop-hp-pavilion-15-b010sw-i3-500gb-windows-8-i3332544805.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 1 549,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 1 549,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332544805/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332544805" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-hp-pavilion-15-b010sw-i3-500gb-windows-8-i3332544805.html"><span>Laptop HP Pavilion 15-B010sw i3 500GB Windows 8</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">23 minuty</strong> Do końca </div>
 <div class="popularity">
    <strong>kupiono  3,
 </strong>
  dostępnych  46 sztuk     </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop HP Pavilion 15-B010sw i3 500GB Windows 8&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332544847" class="offer" data-id="3332544847">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/54/48/3332544847","http://img13.allegroimg.pl/photos/128x96/33/32/54/48/3332544847","http://img13.allegroimg.pl/photos/400x300/33/32/54/48/3332544847"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77919","s":"11339433","1234":"1","4326":"5","4327":"32","4329":"2","4346":"34816","4366":"95","4474":"60","11323":"1"}' >
 <a href="/laptop-hp-compaq-presario-cq58-210sw-500gb-windows-i3332544847.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 1 499,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 1 499,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332544847/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332544847" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-hp-compaq-presario-cq58-210sw-500gb-windows-i3332544847.html"><span>Laptop HP Compaq Presario CQ58-210sw 500GB Windows</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">23 minuty</strong> Do końca </div>
 <div class="popularity">
    <strong>kupiono  1,
 </strong>
  dostępnych  48 sztuk     </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop HP Compaq Presario CQ58-210sw 500GB Windows&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332544889" class="offer" data-id="3332544889">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/54/48/3332544889","http://img13.allegroimg.pl/photos/128x96/33/32/54/48/3332544889","http://img13.allegroimg.pl/photos/400x300/33/32/54/48/3332544889"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77919","s":"11339433","1234":"2","4326":"5","4327":"32","4329":"2","4346":"6334720","4366":"30","4474":"60","11323":"1"}' >
 <a href="/laptop-hp-15-b020sw-i3-3217u-4gb-500-gt630m-1gb-w8-i3332544889.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 1 669,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 1 669,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332544889/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332544889" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-hp-15-b020sw-i3-3217u-4gb-500-gt630m-1gb-w8-i3332544889.html"><span>Laptop HP 15-B020sw i3-3217U 4GB 500 GT630M-1GB W8</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">23 minuty</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  49 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop HP 15-B020sw i3-3217U 4GB 500 GT630M-1GB W8&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332544926" class="offer" data-id="3332544926">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/54/49/3332544926","http://img13.allegroimg.pl/photos/128x96/33/32/54/49/3332544926","http://img13.allegroimg.pl/photos/400x300/33/32/54/49/3332544926"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77917","s":"11339433","1234":"2","4326":"5","4327":"16","4329":"2","4346":"1083648","4366":"20","4474":"60","11323":"1"}' >
 <a href="/laptop-dell-inspiron-15r-7520-i5-3210m-hd7730m-8gb-i3332544926.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 2 799,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 2 799,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332544926/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332544926" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-dell-inspiron-15r-7520-i5-3210m-hd7730m-8gb-i3332544926.html"><span>Laptop DELL Inspiron 15R 7520 i5 3210M HD7730M 8GB</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">23 minuty</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  49 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop DELL Inspiron 15R 7520 i5 3210M HD7730M 8GB&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332545969" class="offer" data-id="3332545969">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/54/59/3332545969","http://img13.allegroimg.pl/photos/128x96/33/32/54/59/3332545969","http://img13.allegroimg.pl/photos/400x300/33/32/54/59/3332545969"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77919","s":"11339433","1234":"2","1235":"1","4326":"5","4327":"32","4329":"2","4346":"6334464","4366":"20","4474":"60","11323":"1"}' >
 <a href="/laptop-hp-envy-6-1110sw-amd-7670-2gb-widi-windows8-i3332545969.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 2 429,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 2 429,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332545969/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332545969" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-hp-envy-6-1110sw-amd-7670-2gb-widi-windows8-i3332545969.html"><span>LAPTOP HP ENVY 6-1110sw AMD 7670 2GB WiDi Windows8</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">24 minuty</strong> Do końca </div>
 <div class="popularity">
    <strong>kupiono  1,
 </strong>
  dostępnych  48 sztuk     </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=LAPTOP HP ENVY 6-1110sw AMD 7670 2GB WiDi Windows8&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332546102" class="offer" data-id="3332546102">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/54/61/3332546102","http://img13.allegroimg.pl/photos/128x96/33/32/54/61/3332546102","http://img13.allegroimg.pl/photos/400x300/33/32/54/61/3332546102"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77917","s":"11339433","1234":"2","4326":"5","4327":"32","4329":"2","4346":"35072","4366":"20","4474":"120","11323":"1"}' >
 <a href="/laptop-dell-xps-15-i5-3210m-gt640m-750gb-windows-8-i3332546102.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 5 899,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 5 899,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332546102/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332546102" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-dell-xps-15-i5-3210m-gt640m-750gb-windows-8-i3332546102.html"><span>Laptop Dell XPS 15 i5 3210M GT640M 750GB Windows 8</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">24 minuty</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  49 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop Dell XPS 15 i5 3210M GT640M 750GB Windows 8&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332590013" class="offer" data-id="3332590013">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/59/00/3332590013","http://img13.allegroimg.pl/photos/128x96/33/32/59/00/3332590013","http://img13.allegroimg.pl/photos/400x300/33/32/59/00/3332590013"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77916","s":"11339433","1234":"2","1235":"1","4326":"8","4327":"32","4329":"2","4346":"6334720","4366":"20","4474":"120","11323":"1"}' >
 <a href="/laptop-asus-r900vj-i5-2x2-5ghz-16gb-gt635m-1tb-i3332590013.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 3 449,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 3 449,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332590013/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332590013" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-asus-r900vj-i5-2x2-5ghz-16gb-gt635m-1tb-i3332590013.html"><span>Laptop ASUS R900VJ i5 2x2,5GHz 16GB GT635M 1TB</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">38 minut</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  30 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop ASUS R900VJ i5 2x2,5GHz 16GB GT635M 1TB&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3331546591" class="offer" data-id="3331546591">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img19.allegroimg.pl/photos/64x48/33/31/54/65/3331546591","http://img19.allegroimg.pl/photos/128x96/33/31/54/65/3331546591","http://img19.allegroimg.pl/photos/400x300/33/31/54/65/3331546591"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77889","s":"15737359","11323":"1"}' >
 <a href="/bk709-lampka-usb-do-laptopa-10-led-gietkie-ramie-i3331546591.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 7,99 <span class="currency">zł</span> </span>
    <span class="delivery">
  <span class="label">z dostawą</span> 12,99 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3331546591/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3331546591" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/bk709-lampka-usb-do-laptopa-10-led-gietkie-ramie-i3331546591.html"><span>bk709 LAMPKA USB do LAPTOPA 10 LED giętkie ramie</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">48 minut</strong> Do końca </div>
 <div class="popularity">
    <strong>kupiono  17,
 </strong>
  dostępne  83 sztuki     </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=bk709 LAMPKA USB do LAPTOPA 10 LED giętkie ramie&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332688878" class="offer" data-id="3332688878">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img17.allegroimg.pl/photos/64x48/33/32/68/88/3332688878","http://img17.allegroimg.pl/photos/128x96/33/32/68/88/3332688878","http://img17.allegroimg.pl/photos/400x300/33/32/68/88/3332688878"],["http://img17.allegroimg.pl/photos/64x48/33/32/68/88/3332688878_1","http://img17.allegroimg.pl/photos/128x96/33/32/68/88/3332688878_1","http://img17.allegroimg.pl/photos/400x300/33/32/68/88/3332688878_1"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77917","s":"2456694","1234":"1","1235":"2","4326":"3","4327":"2","4329":"1","4346":"256","4366":"90","4474":"20","11323":"2"}' >
 <a href="/tani-laptop-panasonic-cf73-cf-73-port-rs-232-com-i3332688878.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 629,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 629,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332688878/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332688878" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/tani-laptop-panasonic-cf73-cf-73-port-rs-232-com-i3332688878.html"><span>TANI LAPTOP PANASONIC CF73 CF-73 PORT RS-232 COM</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">1 godzina</strong> Do końca </div>
 <div class="popularity">
    <strong>kupiono  1,
 </strong>
  dostępnych  49 sztuk     </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=TANI LAPTOP PANASONIC CF73 CF-73 PORT RS-232 COM&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332704560" class="offer" data-id="3332704560">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img17.allegroimg.pl/photos/64x48/33/32/70/45/3332704560","http://img17.allegroimg.pl/photos/128x96/33/32/70/45/3332704560","http://img17.allegroimg.pl/photos/400x300/33/32/70/45/3332704560"],["http://img17.allegroimg.pl/photos/64x48/33/32/70/45/3332704560_1","http://img17.allegroimg.pl/photos/128x96/33/32/70/45/3332704560_1","http://img17.allegroimg.pl/photos/400x300/33/32/70/45/3332704560_1"],["http://img17.allegroimg.pl/photos/64x48/33/32/70/45/3332704560_2","http://img17.allegroimg.pl/photos/128x96/33/32/70/45/3332704560_2","http://img17.allegroimg.pl/photos/400x300/33/32/70/45/3332704560_2"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"101357","s":"10245588","10836":"5","11323":"1"}' >
 <a href="/biurko-stolik-komputerowy-laptop-narozne-okazja-i3332704560.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 119,00 <span class="currency">zł</span> </span>
    <span class="delivery">
  <span class="label">z dostawą</span> 159,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332704560/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332704560" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/biurko-stolik-komputerowy-laptop-narozne-okazja-i3332704560.html"><span>BIURKO STOLIK KOMPUTEROWY LAPTOP NAROŻNE OKAZJA</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">1 godzina</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  30 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=BIURKO STOLIK KOMPUTEROWY LAPTOP NAROŻNE OKAZJA&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332704609" class="offer" data-id="3332704609">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img17.allegroimg.pl/photos/64x48/33/32/70/46/3332704609","http://img17.allegroimg.pl/photos/128x96/33/32/70/46/3332704609","http://img17.allegroimg.pl/photos/400x300/33/32/70/46/3332704609"],["http://img17.allegroimg.pl/photos/64x48/33/32/70/46/3332704609_1","http://img17.allegroimg.pl/photos/128x96/33/32/70/46/3332704609_1","http://img17.allegroimg.pl/photos/400x300/33/32/70/46/3332704609_1"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"101357","s":"10245588","10836":"5","11323":"1"}' >
 <a href="/biurko-komputerowe-pod-laptop-notebook-2-kolory-i3332704609.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 69,00 <span class="currency">zł</span> </span>
    <span class="delivery">
  <span class="label">z dostawą</span> 104,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332704609/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332704609" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/biurko-komputerowe-pod-laptop-notebook-2-kolory-i3332704609.html"><span>BIURKO KOMPUTEROWE POD LAPTOP NOTEBOOK 2 KOLORY</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">1 godzina</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  30 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=BIURKO KOMPUTEROWE POD LAPTOP NOTEBOOK 2 KOLORY&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332706546" class="offer" data-id="3332706546">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img17.allegroimg.pl/photos/64x48/33/32/70/65/3332706546","http://img17.allegroimg.pl/photos/128x96/33/32/70/65/3332706546","http://img17.allegroimg.pl/photos/400x300/33/32/70/65/3332706546"],["http://img17.allegroimg.pl/photos/64x48/33/32/70/65/3332706546_1","http://img17.allegroimg.pl/photos/128x96/33/32/70/65/3332706546_1","http://img17.allegroimg.pl/photos/400x300/33/32/70/65/3332706546_1"],["http://img17.allegroimg.pl/photos/64x48/33/32/70/65/3332706546_2","http://img17.allegroimg.pl/photos/128x96/33/32/70/65/3332706546_2","http://img17.allegroimg.pl/photos/400x300/33/32/70/65/3332706546_2"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"101357","s":"10245588","10836":"4","11323":"1"}' >
 <a href="/biurko-stolik-pod-laptop-regulowana-wysokosc-i3332706546.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 59,00 <span class="currency">zł</span> </span>
    <span class="delivery">
  <span class="label">z dostawą</span> 94,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332706546/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332706546" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/biurko-stolik-pod-laptop-regulowana-wysokosc-i3332706546.html"><span>BIURKO STOLIK POD LAPTOP REGULOWANA WYSOKOŚĆ</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">1 godzina</strong> Do końca </div>
 <div class="popularity">
    <strong>kupiono  3,
 </strong>
  dostępnych  27 sztuk     </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=BIURKO STOLIK POD LAPTOP REGULOWANA WYSOKOŚĆ&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332713326" class="offer" data-id="3332713326">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img17.allegroimg.pl/photos/64x48/33/32/71/33/3332713326","http://img17.allegroimg.pl/photos/128x96/33/32/71/33/3332713326","http://img17.allegroimg.pl/photos/400x300/33/32/71/33/3332713326"],["http://img17.allegroimg.pl/photos/64x48/33/32/71/33/3332713326_1","http://img17.allegroimg.pl/photos/128x96/33/32/71/33/3332713326_1","http://img17.allegroimg.pl/photos/400x300/33/32/71/33/3332713326_1"],["http://img17.allegroimg.pl/photos/64x48/33/32/71/33/3332713326_2","http://img17.allegroimg.pl/photos/128x96/33/32/71/33/3332713326_2","http://img17.allegroimg.pl/photos/400x300/33/32/71/33/3332713326_2"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"101357","s":"10245588","10836":"5","11323":"1"}' >
 <a href="/biurko-stolik-komputerowy-laptop-okazja-i3332713326.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 64,00 <span class="currency">zł</span> </span>
    <span class="delivery">
  <span class="label">z dostawą</span> 99,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332713326/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332713326" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/biurko-stolik-komputerowy-laptop-okazja-i3332713326.html"><span>BIURKO STOLIK KOMPUTEROWY LAPTOP OKAZJA! ! ! !</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">1 godzina</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  30 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=BIURKO STOLIK KOMPUTEROWY LAPTOP OKAZJA! ! ! !&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332714542" class="offer" data-id="3332714542">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img17.allegroimg.pl/photos/64x48/33/32/71/45/3332714542","http://img17.allegroimg.pl/photos/128x96/33/32/71/45/3332714542","http://img17.allegroimg.pl/photos/400x300/33/32/71/45/3332714542"],["http://img17.allegroimg.pl/photos/64x48/33/32/71/45/3332714542_1","http://img17.allegroimg.pl/photos/128x96/33/32/71/45/3332714542_1","http://img17.allegroimg.pl/photos/400x300/33/32/71/45/3332714542_1"],["http://img17.allegroimg.pl/photos/64x48/33/32/71/45/3332714542_2","http://img17.allegroimg.pl/photos/128x96/33/32/71/45/3332714542_2","http://img17.allegroimg.pl/photos/400x300/33/32/71/45/3332714542_2"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"101357","s":"10245588","10836":"5","11323":"1"}' >
 <a href="/biurko-stolik-komputerowy-2-kolory-laptop-netbook-i3332714542.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 71,00 <span class="currency">zł</span> </span>
    <span class="delivery">
  <span class="label">z dostawą</span> 106,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332714542/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332714542" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/biurko-stolik-komputerowy-2-kolory-laptop-netbook-i3332714542.html"><span>BIURKO STOLIK KOMPUTEROWY 2 KOLORY LAPTOP NETBOOK</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">1 godzina</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  30 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=BIURKO STOLIK KOMPUTEROWY 2 KOLORY LAPTOP NETBOOK&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332729968" class="offer" data-id="3332729968">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img17.allegroimg.pl/photos/64x48/33/32/72/99/3332729968","http://img17.allegroimg.pl/photos/128x96/33/32/72/99/3332729968","http://img17.allegroimg.pl/photos/400x300/33/32/72/99/3332729968"],["http://img17.allegroimg.pl/photos/64x48/33/32/72/99/3332729968_1","http://img17.allegroimg.pl/photos/128x96/33/32/72/99/3332729968_1","http://img17.allegroimg.pl/photos/400x300/33/32/72/99/3332729968_1"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77917","s":"2456694","1234":"1","1235":"2","4326":"5","4327":"2","4329":"2","4346":"256","4366":"60","4474":"40","11323":"2"}' >
 <a href="/tani-laptop-stone-core-duo-15-4-2gb-80gb-win-xp-i3332729968.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 549,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 549,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332729968/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332729968" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/tani-laptop-stone-core-duo-15-4-2gb-80gb-win-xp-i3332729968.html"><span>TANI LAPTOP STONE CORE DUO 15,4 2GB 80GB WIN XP</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">1 godzina</strong> Do końca </div>
 <div class="popularity">
    <strong>kupiono  1,
 </strong>
  dostępnych  49 sztuk     </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=TANI LAPTOP STONE CORE DUO 15,4 2GB 80GB WIN XP&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332760125" class="offer" data-id="3332760125">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img19.allegroimg.pl/photos/64x48/33/32/76/01/3332760125","http://img19.allegroimg.pl/photos/128x96/33/32/76/01/3332760125","http://img19.allegroimg.pl/photos/400x300/33/32/76/01/3332760125"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"18609","s":"23408904","11323":"1"}' >
 <a href="/wa4-samochodowy-stolik-pod-laptopa-do-samochodu-i3332760125.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 18,99 <span class="currency">zł</span> </span>
    <span class="delivery">
  <span class="label">z dostawą</span> 33,99 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332760125/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332760125" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/wa4-samochodowy-stolik-pod-laptopa-do-samochodu-i3332760125.html"><span>wa4 Samochodowy STOLIK pod laptopa do samochodu</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">1 godzina</strong> Do końca </div>
 <div class="popularity">
    <strong>kupiono  13,
 </strong>
  dostępnych  87 sztuk     </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=wa4 Samochodowy STOLIK pod laptopa do samochodu&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332776634" class="offer" data-id="3332776634">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img17.allegroimg.pl/photos/64x48/33/32/77/66/3332776634","http://img17.allegroimg.pl/photos/128x96/33/32/77/66/3332776634","http://img17.allegroimg.pl/photos/400x300/33/32/77/66/3332776634"],["http://img17.allegroimg.pl/photos/64x48/33/32/77/66/3332776634_1","http://img17.allegroimg.pl/photos/128x96/33/32/77/66/3332776634_1","http://img17.allegroimg.pl/photos/400x300/33/32/77/66/3332776634_1"],["http://img17.allegroimg.pl/photos/64x48/33/32/77/66/3332776634_2","http://img17.allegroimg.pl/photos/128x96/33/32/77/66/3332776634_2","http://img17.allegroimg.pl/photos/400x300/33/32/77/66/3332776634_2"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"20273","s":"10245588","11323":"1","18167":"16","18196":"12579"}' >
 <a href="/biurko-stolik-komputerowy-laptop-narozne-promocja-i3332776634.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 119,00 <span class="currency">zł</span> </span>
    <span class="delivery">
  <span class="label">z dostawą</span> 159,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332776634/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332776634" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/biurko-stolik-komputerowy-laptop-narozne-promocja-i3332776634.html"><span>BIURKO STOLIK KOMPUTEROWY LAPTOP NAROŻNE PROMOCJA</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">1 godzina</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  30 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=BIURKO STOLIK KOMPUTEROWY LAPTOP NAROŻNE PROMOCJA&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332788590" class="offer" data-id="3332788590">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/78/85/3332788590","http://img13.allegroimg.pl/photos/128x96/33/32/78/85/3332788590","http://img13.allegroimg.pl/photos/400x300/33/32/78/85/3332788590"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77784","s":"11339433","11323":"1"}' >
 <a href="/etui-laptopa-16-18-modecom-brooklyn-czerwone-i3332788590.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 39,00 <span class="currency">zł</span> </span>
    <span class="delivery">
  <span class="label">z dostawą</span> 51,50 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332788590/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332788590" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/etui-laptopa-16-18-modecom-brooklyn-czerwone-i3332788590.html"><span>Etui Laptopa 16-18&#039;&#039; MODECOM Brooklyn czerwone</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">1 godzina</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  49 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Etui Laptopa 16-18&#039;&#039; MODECOM Brooklyn czerwone&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332788677" class="offer" data-id="3332788677">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/78/86/3332788677","http://img13.allegroimg.pl/photos/128x96/33/32/78/86/3332788677","http://img13.allegroimg.pl/photos/400x300/33/32/78/86/3332788677"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77916","s":"11339433","1234":"1","1235":"1","4326":"5","4327":"1","4329":"2","4346":"35072","4366":"95","4474":"60","11323":"1"}' >
 <a href="/laptop-asus-x54c-pentium-2x2-3ghz-4g-500gb-intelhd-i3332788677.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 1 399,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 1 399,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332788677/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332788677" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-asus-x54c-pentium-2x2-3ghz-4g-500gb-intelhd-i3332788677.html"><span>Laptop ASUS X54C Pentium 2x2.3Ghz 4G 500GB IntelHD</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">1 godzina</strong> Do końca </div>
 <div class="popularity">
    <strong>kupiono  2,
 </strong>
  dostępnych  47 sztuk     </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop ASUS X54C Pentium 2x2.3Ghz 4G 500GB IntelHD&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332803032" class="offer" data-id="3332803032">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img17.allegroimg.pl/photos/64x48/33/32/80/30/3332803032","http://img17.allegroimg.pl/photos/128x96/33/32/80/30/3332803032","http://img17.allegroimg.pl/photos/400x300/33/32/80/30/3332803032"],["http://img17.allegroimg.pl/photos/64x48/33/32/80/30/3332803032_1","http://img17.allegroimg.pl/photos/128x96/33/32/80/30/3332803032_1","http://img17.allegroimg.pl/photos/400x300/33/32/80/30/3332803032_1"],["http://img17.allegroimg.pl/photos/64x48/33/32/80/30/3332803032_2","http://img17.allegroimg.pl/photos/128x96/33/32/80/30/3332803032_2","http://img17.allegroimg.pl/photos/400x300/33/32/80/30/3332803032_2"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"20273","s":"10245588","11323":"1","18167":"1","18196":"12551"}' >
 <a href="/biurko-stolik-komputerowy-laptop-netbook-i3332803032.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 64,00 <span class="currency">zł</span> </span>
    <span class="delivery">
  <span class="label">z dostawą</span> 99,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332803032/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332803032" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/biurko-stolik-komputerowy-laptop-netbook-i3332803032.html"><span>BIURKO STOLIK KOMPUTEROWY LAPTOP NETBOOK</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">1 godzina</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  30 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=BIURKO STOLIK KOMPUTEROWY LAPTOP NETBOOK&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332803158" class="offer" data-id="3332803158">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img17.allegroimg.pl/photos/64x48/33/32/80/31/3332803158","http://img17.allegroimg.pl/photos/128x96/33/32/80/31/3332803158","http://img17.allegroimg.pl/photos/400x300/33/32/80/31/3332803158"],["http://img17.allegroimg.pl/photos/64x48/33/32/80/31/3332803158_1","http://img17.allegroimg.pl/photos/128x96/33/32/80/31/3332803158_1","http://img17.allegroimg.pl/photos/400x300/33/32/80/31/3332803158_1"],["http://img17.allegroimg.pl/photos/64x48/33/32/80/31/3332803158_2","http://img17.allegroimg.pl/photos/128x96/33/32/80/31/3332803158_2","http://img17.allegroimg.pl/photos/400x300/33/32/80/31/3332803158_2"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"20273","s":"10245588","11323":"1","18167":"4","18196":"12583"}' >
 <a href="/biurko-stolik-pod-laptop-regulowana-wysokosc-i3332803158.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 59,00 <span class="currency">zł</span> </span>
    <span class="delivery">
  <span class="label">z dostawą</span> 94,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332803158/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332803158" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/biurko-stolik-pod-laptop-regulowana-wysokosc-i3332803158.html"><span>BIURKO STOLIK POD LAPTOP REGULOWANA WYSOKOŚĆ</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">1 godzina</strong> Do końca </div>
 <div class="popularity">
    <strong>kupiono  3,
 </strong>
  dostępne  32 sztuki     </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=BIURKO STOLIK POD LAPTOP REGULOWANA WYSOKOŚĆ&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332803358" class="offer" data-id="3332803358">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img17.allegroimg.pl/photos/64x48/33/32/80/33/3332803358","http://img17.allegroimg.pl/photos/128x96/33/32/80/33/3332803358","http://img17.allegroimg.pl/photos/400x300/33/32/80/33/3332803358"],["http://img17.allegroimg.pl/photos/64x48/33/32/80/33/3332803358_1","http://img17.allegroimg.pl/photos/128x96/33/32/80/33/3332803358_1","http://img17.allegroimg.pl/photos/400x300/33/32/80/33/3332803358_1"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"20273","s":"10245588","11323":"1","18167":"1","18196":"12547"}' >
 <a href="/biurko-komputerowe-pod-laptop-meble-biurowe-okazja-i3332803358.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 69,00 <span class="currency">zł</span> </span>
    <span class="delivery">
  <span class="label">z dostawą</span> 104,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332803358/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332803358" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/biurko-komputerowe-pod-laptop-meble-biurowe-okazja-i3332803358.html"><span>BIURKO KOMPUTEROWE POD LAPTOP MEBLE BIUROWE OKAZJA</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">1 godzina</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  35 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=BIURKO KOMPUTEROWE POD LAPTOP MEBLE BIUROWE OKAZJA&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332813157" class="offer" data-id="3332813157">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/81/31/3332813157","http://img13.allegroimg.pl/photos/128x96/33/32/81/31/3332813157","http://img13.allegroimg.pl/photos/400x300/33/32/81/31/3332813157"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77921","s":"11339433","1234":"2","1235":"1","4326":"5","4327":"16","4329":"2","4346":"7375104","4366":"20","11323":"1"}' >
 <a href="/laptop-msi-ge60-i5-3230m-8gb-500gb-gtx660-2gb-thx-i3332813157.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 2 699,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 2 699,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332813157/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332813157" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-msi-ge60-i5-3230m-8gb-500gb-gtx660-2gb-thx-i3332813157.html"><span>Laptop MSI GE60 i5-3230M 8GB 500GB GTX660 2GB THX</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">2 godziny</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępne  3 sztuki    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop MSI GE60 i5-3230M 8GB 500GB GTX660 2GB THX&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332813313" class="offer" data-id="3332813313">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/81/33/3332813313","http://img13.allegroimg.pl/photos/128x96/33/32/81/33/3332813313","http://img13.allegroimg.pl/photos/400x300/33/32/81/33/3332813313"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77917","s":"11339433","1234":"2","4326":"7","4327":"8","4329":"3","4346":"7383296","4366":"10","11323":"1"}' >
 <a href="/laptop-dell-inspiron-17r-7720-i7-3630qm-gt650m-i3332813313.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 3 899,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 3 899,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332813313/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332813313" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-dell-inspiron-17r-7720-i7-3630qm-gt650m-i3332813313.html"><span>Laptop DELL Inspiron 17R 7720 i7 3630QM GT650M</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">2 godziny</strong> Do końca </div>
 <div class="popularity">
    <strong>kupiono  2,
 </strong>
  dostępnych  47 sztuk     </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop DELL Inspiron 17R 7720 i7 3630QM GT650M&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332813341" class="offer" data-id="3332813341">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/81/33/3332813341","http://img13.allegroimg.pl/photos/128x96/33/32/81/33/3332813341","http://img13.allegroimg.pl/photos/400x300/33/32/81/33/3332813341"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77914","s":"11339433","1234":"2","4326":"7","4327":"32","4329":"2","4346":"6334720","4366":"20","4474":"100","11323":"1"}' >
 <a href="/laptop-acer-aspire-v3-771g-i5-hd-gt630m-2gb-8gb-w8-i3332813341.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 2 649,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 2 649,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332813341/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332813341" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-acer-aspire-v3-771g-i5-hd-gt630m-2gb-8gb-w8-i3332813341.html"><span>Laptop Acer Aspire V3-771G i5 HD GT630M 2GB 8GB W8</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">2 godziny</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  5 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop Acer Aspire V3-771G i5 HD GT630M 2GB 8GB W8&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332813372" class="offer" data-id="3332813372">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/81/33/3332813372","http://img13.allegroimg.pl/photos/128x96/33/32/81/33/3332813372","http://img13.allegroimg.pl/photos/400x300/33/32/81/33/3332813372"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77914","s":"11339433","1234":"2","4326":"7","4327":"32","4329":"2","4346":"35072","4366":"30","4474":"100","11323":"1"}' >
 <a href="/laptop-acer-aspire-v3-771g-33128g50-od-karen-i3332813372.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 2 149,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 2 149,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332813372/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332813372" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-acer-aspire-v3-771g-33128g50-od-karen-i3332813372.html"><span>Laptop Acer Aspire V3-771G-33128G50 od Karen</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">2 godziny</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  49 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop Acer Aspire V3-771G-33128G50 od Karen&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332813388" class="offer" data-id="3332813388">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/81/33/3332813388","http://img13.allegroimg.pl/photos/128x96/33/32/81/33/3332813388","http://img13.allegroimg.pl/photos/400x300/33/32/81/33/3332813388"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77922","s":"11339433","1234":"2","4326":"5","4327":"32","4329":"2","4346":"7383296","4366":"20","4474":"60","11323":"1"}' >
 <a href="/laptop-samsung-550p5c-i5-8gb-1tb-gt630-win8-i3332813388.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 2 489,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 2 489,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332813388/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332813388" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-samsung-550p5c-i5-8gb-1tb-gt630-win8-i3332813388.html"><span>Laptop Samsung 550P5C i5 8GB 1TB GT630 Win8</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">2 godziny</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  49 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop Samsung 550P5C i5 8GB 1TB GT630 Win8&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332813416" class="offer" data-id="3332813416">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/81/34/3332813416","http://img13.allegroimg.pl/photos/128x96/33/32/81/34/3332813416","http://img13.allegroimg.pl/photos/400x300/33/32/81/34/3332813416"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77920","s":"11339433","1234":"2","1235":"1","4326":"5","4327":"32","4329":"3","4346":"6326528","4366":"10","4474":"60","11323":"1"}' >
 <a href="/laptop-lenovo-g580-i7-15-6-4gb-1tb-gt635m-2gb-win8-i3332813416.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 2 489,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 2 489,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332813416/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332813416" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-lenovo-g580-i7-15-6-4gb-1tb-gt635m-2gb-win8-i3332813416.html"><span>Laptop LENOVO G580 i7 15,6 4GB 1TB GT635M_2GB Win8</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">2 godziny</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  49 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop LENOVO G580 i7 15,6 4GB 1TB GT635M_2GB Win8&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332813459" class="offer" data-id="3332813459">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/81/34/3332813459","http://img13.allegroimg.pl/photos/128x96/33/32/81/34/3332813459","http://img13.allegroimg.pl/photos/400x300/33/32/81/34/3332813459"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77920","s":"11339433","1234":"2","1235":"1","4326":"5","4327":"32","4329":"2","4346":"35072","4366":"20","4474":"60","11323":"1"}' >
 <a href="/laptop-lenovo-ideapad-p580-59-349872-8gb-od-karen-i3332813459.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 2 399,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 2 399,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332813459/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332813459" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-lenovo-ideapad-p580-59-349872-8gb-od-karen-i3332813459.html"><span>Laptop Lenovo IdeaPad P580 59-349872 8GB od Karen</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">2 godziny</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  49 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop Lenovo IdeaPad P580 59-349872 8GB od Karen&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332813923" class="offer" data-id="3332813923">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/81/39/3332813923","http://img13.allegroimg.pl/photos/128x96/33/32/81/39/3332813923","http://img13.allegroimg.pl/photos/400x300/33/32/81/39/3332813923"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77916","s":"11339433","1234":"1","1235":"2","4326":"3","4327":"32","4329":"2","4346":"6326528","4366":"20","4474":"60","11323":"1"}' >
 <a href="/lekki-laptop-asus-u32vj-i5-2-5ghz-4g-500gb-win-8-i3332813923.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 2 899,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 2 899,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332813923/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332813923" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/lekki-laptop-asus-u32vj-i5-2-5ghz-4g-500gb-win-8-i3332813923.html"><span>Lekki Laptop ASUS U32VJ i5 2.5Ghz 4G 500GB Win 8</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">2 godziny</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  30 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Lekki Laptop ASUS U32VJ i5 2.5Ghz 4G 500GB Win 8&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332814653" class="offer" data-id="3332814653">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img16.allegroimg.pl/photos/64x48/33/32/81/46/3332814653","http://img16.allegroimg.pl/photos/128x96/33/32/81/46/3332814653","http://img16.allegroimg.pl/photos/400x300/33/32/81/46/3332814653"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77924","s":"4988637","1234":"1","1235":"1","4326":"5","4327":"1","4329":"2","4346":"6334720","4366":"120","4474":"60","11323":"1"}' >
 <a href="/laptop-toshiba-c855-2x1-60ghz-2gb-500gb-100zl-i3332814653.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 1 179,00 <span class="currency">zł</span> </span>
    <span class="delivery">
  <span class="label">z dostawą</span> 1 199,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332814653/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332814653" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-toshiba-c855-2x1-60ghz-2gb-500gb-100zl-i3332814653.html"><span>Laptop Toshiba C855 2x1.60GHz 2GB 500GB + 100zł</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">2 godziny</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  20 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop Toshiba C855 2x1.60GHz 2GB 500GB + 100zł&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332815510" class="offer" data-id="3332815510">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img16.allegroimg.pl/photos/64x48/33/32/81/55/3332815510","http://img16.allegroimg.pl/photos/128x96/33/32/81/55/3332815510","http://img16.allegroimg.pl/photos/400x300/33/32/81/55/3332815510"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77924","s":"4988637","1234":"1","1235":"1","4326":"5","4327":"1","4329":"2","4346":"6334720","4366":"120","4474":"60","11323":"1"}' >
 <a href="/laptop-toshiba-c855-2x1-60ghz-4gb-500gb-100zl-i3332815510.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 1 249,00 <span class="currency">zł</span> </span>
    <span class="delivery">
  <span class="label">z dostawą</span> 1 269,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332815510/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332815510" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-toshiba-c855-2x1-60ghz-4gb-500gb-100zl-i3332815510.html"><span>Laptop Toshiba C855 2x1.60GHz 4GB 500GB + 100zł</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">2 godziny</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  20 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop Toshiba C855 2x1.60GHz 4GB 500GB + 100zł&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332816279" class="offer" data-id="3332816279">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/81/62/3332816279","http://img13.allegroimg.pl/photos/128x96/33/32/81/62/3332816279","http://img13.allegroimg.pl/photos/400x300/33/32/81/62/3332816279"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77924","s":"10639851","1234":"1","1235":"1","4326":"5","4327":"32","4329":"2","4346":"43264","4366":"20","4474":"60","11323":"1"}' >
 <a href="/laptop-toshiba-c855-1rv-i5-6gb-640gb-win8-torba-i3332816279.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 2 169,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 2 169,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332816279/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332816279" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-toshiba-c855-1rv-i5-6gb-640gb-win8-torba-i3332816279.html"><span>Laptop TOSHIBA C855-1RV i5 6GB 640GB WIN8 +torba</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">2 godziny</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  7 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop TOSHIBA C855-1RV i5 6GB 640GB WIN8 +torba&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332816470" class="offer" data-id="3332816470">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/81/64/3332816470","http://img13.allegroimg.pl/photos/128x96/33/32/81/64/3332816470","http://img13.allegroimg.pl/photos/400x300/33/32/81/64/3332816470"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77916","s":"11339433","1234":"1","1235":"1","4326":"5","4327":"1","4329":"2","4346":"6334720","4366":"95","4474":"60","11323":"1"}' >
 <a href="/laptop-asus-x54c-pentium-2x2-3ghz-4g-500gb-intelhd-i3332816470.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 1 399,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 1 399,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332816470/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332816470" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-asus-x54c-pentium-2x2-3ghz-4g-500gb-intelhd-i3332816470.html"><span>Laptop ASUS X54C Pentium 2x2.3Ghz 4G 500GB IntelHD</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">2 godziny</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  30 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop ASUS X54C Pentium 2x2.3Ghz 4G 500GB IntelHD&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332827471" class="offer" data-id="3332827471">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/82/74/3332827471","http://img13.allegroimg.pl/photos/128x96/33/32/82/74/3332827471","http://img13.allegroimg.pl/photos/400x300/33/32/82/74/3332827471"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77920","s":"11339433","1234":"2","1235":"2","4326":"5","4327":"1","4329":"2","4346":"6334720","4366":"30","4474":"60","11323":"1"}' >
 <a href="/laptop-lenovo-ideapad-b590-i3-8gb-500gb-gf610-15-6-i3332827471.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 1 799,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 1 799,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332827471/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332827471" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-lenovo-ideapad-b590-i3-8gb-500gb-gf610-15-6-i3332827471.html"><span>Laptop Lenovo IdeaPad B590 i3 8GB 500GB GF610 15.6</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">2 godziny</strong> Do końca </div>
 <div class="popularity">
    <strong>kupiono  1,
 </strong>
  dostępne  4 sztuki     </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop Lenovo IdeaPad B590 i3 8GB 500GB GF610 15.6&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332827498" class="offer" data-id="3332827498">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/82/74/3332827498","http://img13.allegroimg.pl/photos/128x96/33/32/82/74/3332827498","http://img13.allegroimg.pl/photos/400x300/33/32/82/74/3332827498"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77920","s":"11339433","1234":"1","1235":"1","4326":"5","4327":"1","4329":"2","4346":"6334720","4366":"30","4474":"60","11323":"1"}' >
 <a href="/laptop-lenovo-g580-i3-2348m-4gb-500gb-zestaw-i3332827498.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 1 428,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 1 428,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332827498/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332827498" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-lenovo-g580-i3-2348m-4gb-500gb-zestaw-i3332827498.html"><span>Laptop LENOVO G580 i3-2348M 4GB 500GB + ZESTAW</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">2 godziny</strong> Do końca </div>
 <div class="popularity">
    <strong>kupiono  5,
 </strong>
  dostępne  44 sztuki     </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop LENOVO G580 i3-2348M 4GB 500GB + ZESTAW&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332827530" class="offer" data-id="3332827530">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/82/75/3332827530","http://img13.allegroimg.pl/photos/128x96/33/32/82/75/3332827530","http://img13.allegroimg.pl/photos/400x300/33/32/82/75/3332827530"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77920","s":"11339433","1234":"1","1235":"1","4326":"5","4327":"1","4329":"2","4346":"6334720","4366":"30","4474":"60","11323":"1"}' >
 <a href="/laptop-lenovo-g580-i3-2348m-4gb-500gb-i3332827530.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 1 419,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 1 419,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332827530/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332827530" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-lenovo-g580-i3-2348m-4gb-500gb-i3332827530.html"><span>Laptop LENOVO G580 i3-2348M 4GB 500GB</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">2 godziny</strong> Do końca </div>
 <div class="popularity">
    <strong>kupiono  2,
 </strong>
  dostępnych  47 sztuk     </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop LENOVO G580 i3-2348M 4GB 500GB&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332829415" class="offer" data-id="3332829415">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/82/94/3332829415","http://img13.allegroimg.pl/photos/128x96/33/32/82/94/3332829415","http://img13.allegroimg.pl/photos/400x300/33/32/82/94/3332829415"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77785","s":"11339433","11323":"1"}' >
 <a href="/torba-na-laptop-16-cali-d-lex-lx-080pf-bk-czarna-i3332829415.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 64,90 <span class="currency">zł</span> </span>
    <span class="delivery">
  <span class="label">z dostawą</span> 77,40 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332829415/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332829415" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/torba-na-laptop-16-cali-d-lex-lx-080pf-bk-czarna-i3332829415.html"><span>Torba na laptop 16 cali D-Lex LX-080PF-BK Czarna</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">2 godziny</strong> Do końca </div>
 <div class="popularity">
    <strong>kupiono  1,
 </strong>
  dostępnych  29 sztuk     </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Torba na laptop 16 cali D-Lex LX-080PF-BK Czarna&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332829440" class="offer" data-id="3332829440">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/82/94/3332829440","http://img13.allegroimg.pl/photos/128x96/33/32/82/94/3332829440","http://img13.allegroimg.pl/photos/400x300/33/32/82/94/3332829440"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77784","s":"11339433","11323":"1"}' >
 <a href="/etui-laptopa-16-18-modecom-brooklyn-czerwone-i3332829440.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 17,00 <span class="currency">zł</span> </span>
    <span class="delivery">
  <span class="label">z dostawą</span> 29,50 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332829440/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332829440" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/etui-laptopa-16-18-modecom-brooklyn-czerwone-i3332829440.html"><span>Etui Laptopa 16-18&#039;&#039; MODECOM Brooklyn Czerwone</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">2 godziny</strong> Do końca </div>
 <div class="popularity">
    <strong>kupiono  3,
 </strong>
  dostępnych  27 sztuk     </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Etui Laptopa 16-18&#039;&#039; MODECOM Brooklyn Czerwone&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332829468" class="offer" data-id="3332829468">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/82/94/3332829468","http://img13.allegroimg.pl/photos/128x96/33/32/82/94/3332829468","http://img13.allegroimg.pl/photos/400x300/33/32/82/94/3332829468"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77785","s":"11339433","11323":"1"}' >
 <a href="/torba-laptopa-15-4-d-lex-skorzana-lx-501fl-i3332829468.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 349,00 <span class="currency">zł</span> </span>
    <span class="delivery">
  <span class="label">z dostawą</span> 361,50 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332829468/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332829468" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/torba-laptopa-15-4-d-lex-skorzana-lx-501fl-i3332829468.html"><span>Torba Laptopa 15,4&#039;&#039; D-Lex skórzana LX-501FL</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">2 godziny</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  30 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Torba Laptopa 15,4&#039;&#039; D-Lex skórzana LX-501FL&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332830584" class="offer" data-id="3332830584">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/83/05/3332830584","http://img13.allegroimg.pl/photos/128x96/33/32/83/05/3332830584","http://img13.allegroimg.pl/photos/400x300/33/32/83/05/3332830584"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77920","s":"11339433","1234":"2","1235":"1","4326":"7","4327":"32","4329":"3","4346":"6334720","4366":"10","4474":"100","11323":"1"}' >
 <a href="/laptop-lenovo-g780a-i7-12gb-1tb-gt635m-win8-i3332830584.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 3 049,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 3 049,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332830584/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332830584" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-lenovo-g780a-i7-12gb-1tb-gt635m-win8-i3332830584.html"><span>Laptop LENOVO G780A i7 12GB 1TB GT635M Win8</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">2 godziny</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  49 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop LENOVO G780A i7 12GB 1TB GT635M Win8&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332830608" class="offer" data-id="3332830608">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/83/06/3332830608","http://img13.allegroimg.pl/photos/128x96/33/32/83/06/3332830608","http://img13.allegroimg.pl/photos/400x300/33/32/83/06/3332830608"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77914","s":"11339433","1234":"2","4326":"7","4327":"32","4329":"2","4346":"6326528","4366":"20","4474":"100","11323":"1"}' >
 <a href="/laptop-acer-i5-3-1ghz-turbo-1000gb-12gb-gt630-win-i3332830608.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 2 819,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 2 819,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332830608/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332830608" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-acer-i5-3-1ghz-turbo-1000gb-12gb-gt630-win-i3332830608.html"><span>Laptop Acer i5 3.1Ghz TURBO 1000GB 12GB GT630 Win</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">2 godziny</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  49 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop Acer i5 3.1Ghz TURBO 1000GB 12GB GT630 Win&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332830633" class="offer" data-id="3332830633">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/83/06/3332830633","http://img13.allegroimg.pl/photos/128x96/33/32/83/06/3332830633","http://img13.allegroimg.pl/photos/400x300/33/32/83/06/3332830633"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77914","s":"11339433","1234":"2","4326":"7","4327":"32","4329":"2","4346":"35072","4366":"20","4474":"100","11323":"1"}' >
 <a href="/laptop-acer-i5-3-1ghz-turbo-1000gb-16gb-gt630-win-i3332830633.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 2 999,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 2 999,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332830633/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332830633" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-acer-i5-3-1ghz-turbo-1000gb-16gb-gt630-win-i3332830633.html"><span>Laptop Acer i5 3.1Ghz TURBO 1000GB 16GB GT630 Win</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">2 godziny</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  49 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop Acer i5 3.1Ghz TURBO 1000GB 16GB GT630 Win&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332830663" class="offer" data-id="3332830663">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/83/06/3332830663","http://img13.allegroimg.pl/photos/128x96/33/32/83/06/3332830663","http://img13.allegroimg.pl/photos/400x300/33/32/83/06/3332830663"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77920","s":"11339433","1234":"1","1235":"1","4326":"5","4327":"32","4329":"2","4346":"6334720","4366":"95","4474":"60","11323":"1"}' >
 <a href="/laptop-lenovo-g580-2x2-2ghz-8gb-500-win8-i3332830663.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 1 589,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 1 589,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332830663/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332830663" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-lenovo-g580-2x2-2ghz-8gb-500-win8-i3332830663.html"><span>Laptop LENOVO G580 2x2.2GHz 8GB 500 Win8</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">2 godziny</strong> Do końca </div>
 <div class="popularity">
    <strong>kupiono  1,
 </strong>
  dostępnych  48 sztuk     </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop LENOVO G580 2x2.2GHz 8GB 500 Win8&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332830727" class="offer" data-id="3332830727">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/83/07/3332830727","http://img13.allegroimg.pl/photos/128x96/33/32/83/07/3332830727","http://img13.allegroimg.pl/photos/400x300/33/32/83/07/3332830727"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77922","s":"11339433","1234":"2","1235":"2","4326":"7","4327":"32","4329":"3","4346":"6334720","4366":"10","4474":"100","11323":"1"}' >
 <a href="/laptop-samsung-np350e7c-i7-3630qm-windows-8-matowa-i3332830727.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 2 649,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 2 649,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332830727/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332830727" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-samsung-np350e7c-i7-3630qm-windows-8-matowa-i3332830727.html"><span>Laptop Samsung NP350E7C i7-3630QM Windows 8 MATOWA</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">2 godziny</strong> Do końca </div>
 <div class="popularity">
    <strong>kupiono  1,
 </strong>
  dostępnych  48 sztuk     </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop Samsung NP350E7C i7-3630QM Windows 8 MATOWA&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332845610" class="offer" data-id="3332845610">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/84/56/3332845610","http://img13.allegroimg.pl/photos/128x96/33/32/84/56/3332845610","http://img13.allegroimg.pl/photos/400x300/33/32/84/56/3332845610"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77919","s":"11339433","1234":"2","4326":"5","4327":"32","4329":"2","4346":"34816","4366":"20","4474":"60","11323":"1"}' >
 <a href="/laptop-hp-pavilion-i5-3230m-hd7670m-750gb-windows-i3332845610.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 2 299,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 2 299,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332845610/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332845610" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-hp-pavilion-i5-3230m-hd7670m-750gb-windows-i3332845610.html"><span>LAPTOP HP Pavilion i5-3230M  HD7670M 750GB Windows</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">2 godziny</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  49 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=LAPTOP HP Pavilion i5-3230M  HD7670M 750GB Windows&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3293924854" class="offer promo-bold" data-id="3293924854">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img02.allegroimg.pl/photos/64x48/32/93/92/48/3293924854","http://img02.allegroimg.pl/photos/128x96/32/93/92/48/3293924854","http://img02.allegroimg.pl/photos/400x300/32/93/92/48/3293924854"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77756","s":"11406155","11323":"1","18448":"4"}' >
 <a href="/bateria-laptopa-dell-inspiron-1464-1564-1764-jkvc5-i3293924854.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 159,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 159,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3293924854/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3293924854" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/bateria-laptopa-dell-inspiron-1464-1564-1764-jkvc5-i3293924854.html"><span>Bateria laptopa DELL Inspiron 1464 1564 1764 JKVC5</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">2 godziny</strong> Do końca </div>
 <div class="popularity">
    <strong>kupiono  5,
 </strong>
  dostępnych  15 sztuk     </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Bateria laptopa DELL Inspiron 1464 1564 1764 JKVC5&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332876615" class="offer" data-id="3332876615">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img18.allegroimg.pl/photos/64x48/33/32/87/66/3332876615","http://img18.allegroimg.pl/photos/128x96/33/32/87/66/3332876615","http://img18.allegroimg.pl/photos/400x300/33/32/87/66/3332876615"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77914","s":"421805","1234":"2","1235":"3","4326":"5","4327":"32","4329":"2","4346":"6334720","4366":"30","4474":"60","11323":"1"}' >
 <a href="/laptop-acer-v5-571pg-i3-16g-500g-gt710-win8-dotyk-i3332876615.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 2 749,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 2 749,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332876615/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332876615" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-acer-v5-571pg-i3-16g-500g-gt710-win8-dotyk-i3332876615.html"><span>Laptop Acer V5-571PG i3 16G 500G GT710 Win8 DOTYK!</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">2 godziny</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  150 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop Acer V5-571PG i3 16G 500G GT710 Win8 DOTYK!&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332876612" class="offer" data-id="3332876612">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img18.allegroimg.pl/photos/64x48/33/32/87/66/3332876612","http://img18.allegroimg.pl/photos/128x96/33/32/87/66/3332876612","http://img18.allegroimg.pl/photos/400x300/33/32/87/66/3332876612"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77914","s":"421805","1234":"2","1235":"3","4326":"5","4327":"32","4329":"2","4346":"6334720","4366":"30","4474":"60","11323":"1"}' >
 <a href="/laptop-acer-v5-571pg-i3-12g-500g-gt710-win8-dotyk-i3332876612.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 2 649,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 2 649,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332876612/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332876612" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-acer-v5-571pg-i3-12g-500g-gt710-win8-dotyk-i3332876612.html"><span>Laptop Acer V5-571PG i3 12G 500G GT710 Win8 DOTYK!</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">2 godziny</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  150 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop Acer V5-571PG i3 12G 500G GT710 Win8 DOTYK!&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332876628" class="offer" data-id="3332876628">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img18.allegroimg.pl/photos/64x48/33/32/87/66/3332876628","http://img18.allegroimg.pl/photos/128x96/33/32/87/66/3332876628","http://img18.allegroimg.pl/photos/400x300/33/32/87/66/3332876628"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77914","s":"421805","1234":"2","1235":"3","4326":"5","4327":"32","4329":"2","4346":"6334720","4366":"30","4474":"60","11323":"1"}' >
 <a href="/laptop-acer-v5-571pg-i3-8g-500g-gt710-win8-dotyk-i3332876628.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 2 549,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 2 549,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332876628/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332876628" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-acer-v5-571pg-i3-8g-500g-gt710-win8-dotyk-i3332876628.html"><span>Laptop Acer V5-571PG i3 8G 500G GT710 Win8 DOTYK!</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">2 godziny</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  150 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop Acer V5-571PG i3 8G 500G GT710 Win8 DOTYK!&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332876662" class="offer" data-id="3332876662">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img18.allegroimg.pl/photos/64x48/33/32/87/66/3332876662","http://img18.allegroimg.pl/photos/128x96/33/32/87/66/3332876662","http://img18.allegroimg.pl/photos/400x300/33/32/87/66/3332876662"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77914","s":"421805","1234":"2","1235":"3","4326":"5","4327":"32","4329":"2","4346":"6334720","4366":"30","4474":"60","11323":"1"}' >
 <a href="/laptop-acer-v5-571pg-i3-4g-500g-gt710-win8-dotyk-i3332876662.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 2 499,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 2 499,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332876662/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332876662" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-acer-v5-571pg-i3-4g-500g-gt710-win8-dotyk-i3332876662.html"><span>Laptop Acer V5-571PG i3 4G 500G GT710 Win8 DOTYK!</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">2 godziny</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  150 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Laptop Acer V5-571PG i3 4G 500G GT710 Win8 DOTYK!&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332874831" class="offer" data-id="3332874831">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/87/48/3332874831","http://img13.allegroimg.pl/photos/128x96/33/32/87/48/3332874831","http://img13.allegroimg.pl/photos/400x300/33/32/87/48/3332874831"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"4576","s":"11339433","11323":"1"}' >
 <a href="/myszka-logitech-m115-black-mouse-mysz-laptop-i3332874831.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 36,00 <span class="currency">zł</span> </span>
    <span class="delivery">
  <span class="label">z dostawą</span> 48,50 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332874831/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332874831" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/myszka-logitech-m115-black-mouse-mysz-laptop-i3332874831.html"><span>Myszka Logitech M115 Black Mouse Mysz Laptop</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">2 godziny</strong> Do końca </div>
 <div class="popularity">
    <strong>kupiono  4,
 </strong>
  dostępnych  45 sztuk     </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=Myszka Logitech M115 Black Mouse Mysz Laptop&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
<article id="item-3332874858" class="offer" data-id="3332874858">
 <div class="excerpt">
 <div class="photo loading" data-img='[["http://img13.allegroimg.pl/photos/64x48/33/32/87/48/3332874858","http://img13.allegroimg.pl/photos/128x96/33/32/87/48/3332874858","http://img13.allegroimg.pl/photos/400x300/33/32/87/48/3332874858"]]' data-external='[0]' data-hidetooltip='' data-popup='{"a":"0","b":"1","c":"77917","s":"11339433","1234":"2","4326":"7","4327":"32","4329":"2","4346":"35072","4366":"30","4474":"100","11323":"1"}' >
 <a href="/laptop-dell-inspiron-17r-2-4gh-12gb-750gb-gt630-w8-i3332874858.html"><span class="inner"></span></a>
 </div>
 <div class="purchase">
 <div class="price">
   <span class="buy-now dist">

 <span class="label">Kup Teraz</span> 2 599,00 <span class="currency">zł</span> </span>
    <span class="delivery">
 <span class="item-ico item-fs icon-fs">wysyłka GRATIS</span> <span class="label">z dostawą</span> 2 599,00 <span class="currency">zł</span> </span>
  </div>
   <a href="/Cart.php/add/id,3332874858/sesstoken,cfab3fa6ddb2ab8147e78b0365bb3213" class="item-cart primary-btn btn disabled" data-id="3332874858" data-cartid="" data-sesstoken="cfab3fa6ddb2ab8147e78b0365bb3213"><span>do koszyka</span></a>
  <a href="#" class="item-watch" data-lang="obserwujesz"><span>obserwuj</span></a>
  </div>
  <div class="details">
 <header>
 <span class="item-ico item-sa icon-as">Standard Allegro</span> <h2><a href="/laptop-dell-inspiron-17r-2-4gh-12gb-750gb-gt630-w8-i3332874858.html"><span>LAPTOP DELL Inspiron 17R 2,4GH 12GB 750GB GT630 W8</span></a></h2>
 </header>
 <div class="params params-all"></div>
 <div class="params params-featured">
 <dl></dl>
 </div>
 <div class="expiry">
 <strong class="ending">2 godziny</strong> Do końca </div>
 <div class="popularity">
     wciąż dostępnych  49 sztuk    </div>
 </div>
 <div class="ad-details">



  </div>
 <div class="products">
  <div class="user"></div>
  <a class="find-similar" href="/listing/listing.php?string=LAPTOP DELL Inspiron 17R 2,4GH 12GB 750GB GT630 W8&similar=1&order=xd&link=1"><span>Podobne oferty</span></a>
  </div>
 </div>
</article>
 </section>
 <div class="listing-options-bottom">
   <div class="items-per-page">
 <ul>
  <li class="current"><span>60</span></li>
  <li><a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&limit=120&offerTypeBuyNow=1&standard_allegro=1&string=laptop"><span>120</span></a></li>
  <li><a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&limit=180&offerTypeBuyNow=1&standard_allegro=1&string=laptop"><span>180</span></a></li>
  <li><span class="label">ofert na stronie</span></li>
 </ul>
 </div> <div class="pager pager-bottom">
 <ul class="pager-nav">


   <li class="current"><span>1</span></li>
    <li><a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&offerTypeBuyNow=1&p=2&standard_allegro=1&string=laptop"><span>2</span></a></li>
    <li><a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&offerTypeBuyNow=1&p=3&standard_allegro=1&string=laptop"><span>3</span></a></li>
    <li><a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&offerTypeBuyNow=1&p=4&standard_allegro=1&string=laptop"><span>4</span></a></li>
    <li><a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&offerTypeBuyNow=1&p=5&standard_allegro=1&string=laptop"><span>5</span></a></li>
   <li class="suffix"><span>z</span></li>
 <li><a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&offerTypeBuyNow=1&p=23&standard_allegro=1&string=laptop"><span>23</span></a></li>

  <li class="next"><a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&offerTypeBuyNow=1&p=2&standard_allegro=1&string=laptop"><span>następna</span><span class="arrow">&gt;</span></a></li>
  </ul>
</div>
  </div>
</div>

<section id="listing-message-modal" class="modal listing-message-modal hide fade">
 <div class="modal-header">
 <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
 <h3></h3>
 </div>
 <div class="modal-body"></div>
</section>

<a id="go-to-top" class="go-to-top hidden" href="#"></a>

 <div class="recommended-listing">
 <div class="vela">
 <section class="recommended items-box carousel-box loading" id="items-carousel-recommended" data-url='http://recommend.allegro.pl/?sId[0]=16&caLvl1=0&caLvl2=0&caLvl3=0&caLvl4=0&cId[0]=8007342&cId[1]=8011513&cId[2]=7949230&cId[3]=8021867&cId[4]=16528&cId[5]=8016037&cId[6]=8012644&cId[7]=8020108&cId[8]=8023783&cId[9]=8015052&uId=&uHash=N55404c37daa61ee09d4235553d244de6'>
 <h2>otwórz się na <span>inne pomysły</span></h2>

 <div class="items-carousel">
 <div class="carousel-nav">
 <a class="sprite carousel-prev" title="Poprzednia strona" href="#carousel-prev">
 Poprzednia strona </a>
 <a class="sprite carousel-next" title="Następna strona" href="#carousel-next">
 Następna strona </a>
 </div>
 <ul class="items-wrap"></ul>
 </div>
 </section>
</div> </div>
 <script id="items-carousel-template-recommended" type="text/template">

 <li>
 <a href="/ShowItem2.php?item=<%= itemId %>&ars_source=ars&ars_socket_id=<%= socketId %>&ars_rule_id=<%= ruleId %>" title="<%= itemName %>" class="photo">
 <% if (photoLink) { %>
 <img src="<%= photoLink %>" width="128" height="96" alt="<%= itemName %>">
 <% } else { %>
 <span class="no-photo"></span>
 <% } %>
 </a>
 <% if (standard) { %><i class="icon-as"></i><% } %>
 <h3><a href="/ShowItem2.php?item=<%= itemId %>&ars_source=ars&ars_socket_id=<%= socketId %>&ars_rule_id=<%= ruleId %>"><span><%= itemName %></span></a></h3>

 <span class="price">
 <% if (buyNowPrice != 0) { %>
 <span class="buy-now">Kup Teraz</span><%= utils.formatPrice(buyNowPrice, priceFormat) %>
 <% } else { %>
 od <%= utils.formatPrice(bidPrice, priceFormat)%>
 <% } %>
 <% if (freeShipping) { %>
 <i class="icon-fs"></i>
 <% } %>
 </span>
 </li>

</script>

<script id="listing-icon-info" type="text/template">
{
 "standardAllegro": "<a href=\"http:\/\/uslugi.allegro.pl\/sa\/\" target=\"_blank\">Standard Allegro<\/a> to gwarancja udanej transakcji. Oznacza najwy\u017csz\u0105 jako\u015b\u0107 obs\u0142ugi klienta. O wyr\u00f3\u017cnieniu oferty w ten spos\u00f3b decyduj\u0105 nasze okre\u015blone kryteria oraz opinie kupuj\u0105cych.",
 "freeShipping": "<a href=\"http:\/\/uslugi.allegro.pl\/wg\/\" target=\"_blank\">Wysy\u0142ka Gratis<\/a> to co najmniej jedna darmowa opcja dostawy. W ten spos\u00f3b wygodniej dokonasz transakcji. Bez dodatkowych koszt\u00f3w!",
 "loyaltyProgram": ""}
</script>

<!-- saddr: 94-46-->
<!-- site: 1/0 -->


<!-- Footer start -->
 </div> <!-- /pagecontent1 -->

 <div class="vela">
 <div class="main-footer">
 <div class="clearfix">
 <p class="main-footer-logo">
 <a href="http://allegro.pl/">
 <img title="Allegro.pl - Więcej niż aukcje. Najlepsze oferty na największej platformie handlowej." src="http://static.allegrostatic.pl/site_images/1/0/vela/allegro-logo-small.png" width="67" width="23" alt="allegro">
 </a>
 </p>

 <ul class="main-footer-shortcuts">
  <li>
 <a class="" href="http://cafe.allegro.pl/">Cafe</a>
 </li>
  <li>
 <a class="" href="http://allegro.pl/country_pages/1/0/marketing/about.php">O nas</a>
 </li>
  <li>
 <a class="" href="http://kariera.allegro.pl/">Praca</a>
 </li>
  <li>
 <a class="" href="http://poznaj.allegro.pl/">Poznaj Allegro</a>
 </li>
  <li>
 <a class="" href="http://allegro.pl/country_pages/1/0/user_agreement.php">Regulamin</a>
 </li>
  <li>
 <a class=" open-help" href="javascript:OpenHelp()">Pomoc</a>
 </li>
  <li>
 <a class="" href="http://m.allegro.pl/">Wersja Mobilna</a>
 </li>
  </ul>
 </div>
 </div>
</div>



<p class="reg">
  Korzystanie z serwisu oznacza akceptację  <a href="http://allegro.pl/country_pages/1/0/user_agreement.php" class="alleLink"><span>regulaminu</span></a>
 <br /><a href="http://allegro.pl/country_pages/1/0/cookie_policy.php" class="alleLink"><span>Informacja o cookies</span></a>
</p>

 </div><!-- /footerContentBox -->

<script type="text/javascript">
<!--//--><![CDATA[//><!--
var gemius_identifier = new String('0iTgIucYowHxbRZHgZUtHeUUP_fFZCMccPZmta45O.b.87');
//--><!]]>
</script>
<script type="text/javascript" src="http://static.allegrostatic.pl/js/xgemius.js"></script>


<script type = "text/javascript">
<!--//--><![CDATA[//><!--
var _cm = {
 "baseUrl":('https:' == document.location.protocol ? 'https://' : 'http://') + 'ngacm.com/',

 "pv": true,
 "account": "CM.991213.tz_pl",
 "domain": ".allegro.pl"

};

(function() {
 var cm = document.createElement('script'); cm.type = 'text/javascript'; cm.async = true;
  cm.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'ngastatic.com/s4c/collect.js';
  var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(cm, s);
})();
//--><!]]>
</script>

  <script type="text/javascript" src="http://static.allegrostatic.pl/site_images/1/0/js/ado.js"></script>

<script src="http://static.allegrostatic.pl/js/libs/jquery-1.8.3_av.2013.37.4.min.js" type="text/javascript" charset="utf-8"></script>
<script type="text/javascript" charset="utf-8">var $j = jQuery.noConflict();</script>
<script src="http://static.allegrostatic.pl/js/libs/jquery-ui-1.9.2.custom_av.2013.37.4.min.js" type="text/javascript" charset="utf-8"></script>
<script src="http://static.allegrostatic.pl/js/libs/require-2.1.1_av.2013.37.4.min.js" type="text/javascript" charset="utf-8"></script>
<script src="http://static.allegrostatic.pl/js/libs/slimScroll_av.2013.37.4.min.js" type="text/javascript" charset="utf-8"></script>
<script src="http://static.allegrostatic.pl/js/scripts/jq_plugins_av.2013.37.4.min.js" type="text/javascript" charset="utf-8"></script>
<script src="http://static.allegrostatic.pl/js/scripts/mainjs-5_av.2013.37.4.min.js" type="text/javascript" charset="utf-8"></script>
<script src="http://static.allegrostatic.pl/js/scripts/vela-listing_av.2013.37.4.min.js" type="text/javascript" charset="utf-8"></script>
<script type="text/javascript">
//<![CDATA[

jQuery(function () {
require.config({"paths":{"async":"libs\/require-async","text":"libs\/require-text","tpl":"libs\/require-tpl","jquery":"libs\/jquery-1.8.3.min","jquery.ui":"libs\/jquery-ui-1.7.2.min","jquery.scrollTo":"libs\/jquery.scrollTo.min","jquery.multiSelect":"libs\/jquery.multi-select.min","jquery.simpleTree":"libs\/jquery.simpleTree.min","jquery.itemList":"libs\/jquery.itemList.min","underscore":"libs\/underscore.min","underscore.string":"libs\/underscore.string.min","backbone":"libs\/backbone.min","backbone.validation":"libs\/backbone.validation-amd.min","backbone.validation-msg-extension":"\/js\/scripts\/backbone.validation-msg-extension","backbone.validation-rules-extension":"\/js\/scripts\/backbone.validation-rules-extension","bootstrap":"\/js\/libs\/bootstrap.min","bootstrap-modal-extensions":"\/js\/scripts\/bootstrap-modal-extensions","accounting":"\/js\/libs\/accounting.min","marker-clusterer":"libs\/markerclusterer.min","collections":"scripts\/items-carousel\/collections","views":"scripts\/items-carousel\/views","main":"scripts\/items-carousel\/build\/items-carousel_av.2013.37.4.min"},"shim":{"jquery":{"exports":"jQuery"},"jquery.ui":{"deps":["jquery"]},"jquery.scrollTo":{"deps":["jquery"],"exports":"jQuery.fn.scrollTo"},"jquery.multiSelect":{"deps":["jquery"],"exports":"jQuery.fn.multiSelect"},"jquery.simpleTree":{"deps":["jquery"],"exports":"jQuery.fn.simpleTree"},"jquery.itemList":{"deps":["jquery"],"exports":"jQuery.fn.scrollTo"},"underscore":{"exports":"_"},"underscore.string":{"deps":["underscore"],"exports":"_s"},"backbone":{"deps":["jquery","underscore"],"exports":"Backbone"},"backbone.validation":{"deps":["backbone"]},"backbone.validation-msg-extension":{"deps":["backbone.validation"]},"backbone.validation-rules-extension":{"deps":["backbone.validation"]},"bootstrap-modal-extensions":{"deps":["bootstrap"]},"marker-clusterer":{"deps":["async!https:\/\/maps.google.com\/maps\/api\/js?sensor=false"],"exports":"MarkerClusterer"}},"baseUrl":"http:\/\/static.allegrostatic.pl\/js"});
define('jquery', function () { return jQuery; });
require.config({config:{text:{useXhr:function(){return true;}}}});
require(['main']);
});
jQuery(function () {
require.config({"paths":{"async":"libs\/require-async","text":"libs\/require-text","tpl":"libs\/require-tpl","jquery":"libs\/jquery-1.8.3.min","jquery.ui":"libs\/jquery-ui-1.7.2.min","jquery.scrollTo":"libs\/jquery.scrollTo.min","jquery.multiSelect":"libs\/jquery.multi-select.min","jquery.simpleTree":"libs\/jquery.simpleTree.min","jquery.itemList":"libs\/jquery.itemList.min","underscore":"libs\/underscore.min","underscore.string":"libs\/underscore.string.min","backbone":"libs\/backbone.min","backbone.validation":"libs\/backbone.validation-amd.min","backbone.validation-msg-extension":"\/js\/scripts\/backbone.validation-msg-extension","backbone.validation-rules-extension":"\/js\/scripts\/backbone.validation-rules-extension","bootstrap":"\/js\/libs\/bootstrap.min","bootstrap-modal-extensions":"\/js\/scripts\/bootstrap-modal-extensions","accounting":"\/js\/libs\/accounting.min","marker-clusterer":"libs\/markerclusterer.min","models":"scripts\/listing\/models","views":"scripts\/listing\/views","listing":"scripts\/listing\/build\/listing_av.2013.37.4.min"},"shim":{"jquery":{"exports":"jQuery"},"jquery.ui":{"deps":["jquery"]},"jquery.scrollTo":{"deps":["jquery"],"exports":"jQuery.fn.scrollTo"},"jquery.multiSelect":{"deps":["jquery"],"exports":"jQuery.fn.multiSelect"},"jquery.simpleTree":{"deps":["jquery"],"exports":"jQuery.fn.simpleTree"},"jquery.itemList":{"deps":["jquery"],"exports":"jQuery.fn.scrollTo"},"underscore":{"exports":"_"},"underscore.string":{"deps":["underscore"],"exports":"_s"},"backbone":{"deps":["jquery","underscore"],"exports":"Backbone"},"backbone.validation":{"deps":["backbone"]},"backbone.validation-msg-extension":{"deps":["backbone.validation"]},"backbone.validation-rules-extension":{"deps":["backbone.validation"]},"bootstrap-modal-extensions":{"deps":["bootstrap"]},"marker-clusterer":{"deps":["async!https:\/\/maps.google.com\/maps\/api\/js?sensor=false"],"exports":"MarkerClusterer"}},"baseUrl":"http:\/\/static.allegrostatic.pl\/js"});
define('jquery', function () { return jQuery; });
require.config({config:{text:{useXhr:function(){return true;}}}});
require(['listing']);
});
jQuery(function () {
require.config({"paths":{"async":"libs\/require-async","text":"libs\/require-text","tpl":"libs\/require-tpl","jquery":"libs\/jquery-1.8.3.min","jquery.ui":"libs\/jquery-ui-1.7.2.min","jquery.scrollTo":"libs\/jquery.scrollTo.min","jquery.multiSelect":"libs\/jquery.multi-select.min","jquery.simpleTree":"libs\/jquery.simpleTree.min","jquery.itemList":"libs\/jquery.itemList.min","underscore":"libs\/underscore.min","underscore.string":"libs\/underscore.string.min","backbone":"libs\/backbone.min","backbone.validation":"libs\/backbone.validation-amd.min","backbone.validation-msg-extension":"\/js\/scripts\/backbone.validation-msg-extension","backbone.validation-rules-extension":"\/js\/scripts\/backbone.validation-rules-extension","bootstrap":"\/js\/libs\/bootstrap.min","bootstrap-modal-extensions":"\/js\/scripts\/bootstrap-modal-extensions","accounting":"\/js\/libs\/accounting.min","marker-clusterer":"libs\/markerclusterer.min","vela-layout":"scripts\/vela-layout\/build\/vela-layout_av.2013.37.4.min"},"shim":{"jquery":{"exports":"jQuery"},"jquery.ui":{"deps":["jquery"]},"jquery.scrollTo":{"deps":["jquery"],"exports":"jQuery.fn.scrollTo"},"jquery.multiSelect":{"deps":["jquery"],"exports":"jQuery.fn.multiSelect"},"jquery.simpleTree":{"deps":["jquery"],"exports":"jQuery.fn.simpleTree"},"jquery.itemList":{"deps":["jquery"],"exports":"jQuery.fn.scrollTo"},"underscore":{"exports":"_"},"underscore.string":{"deps":["underscore"],"exports":"_s"},"backbone":{"deps":["jquery","underscore"],"exports":"Backbone"},"backbone.validation":{"deps":["backbone"]},"backbone.validation-msg-extension":{"deps":["backbone.validation"]},"backbone.validation-rules-extension":{"deps":["backbone.validation"]},"bootstrap-modal-extensions":{"deps":["bootstrap"]},"marker-clusterer":{"deps":["async!https:\/\/maps.google.com\/maps\/api\/js?sensor=false"],"exports":"MarkerClusterer"}},"baseUrl":"http:\/\/static.allegrostatic.pl\/js"});
define('jquery', function () { return jQuery; });
require.config({config:{text:{useXhr:function(){return true;}}}});
require(['vela-layout']);
});
$j("a[rel=external]").attr("target","_blank");

if(typeof ado!=="object"){ado={};ado.config=ado.preview=ado.placement=ado.master=ado.slave=function(){};}
ado.config({mode: "new", xml: false, characterEncoding: true});

/* (c)AdOcean 2003-2011 */




 var _adoCalls = _adoCalls || [];
 var _cmParams = _cmParams || [];

 var allAdocean = {
 'intervalCount' : 0,
 'interval' : null,
 'showAds' : function() {
 allAdocean.interval = setInterval(
 function() {
 $j('[data-adocean-id]').each(
 function() {
 if ($j(this).find('[data-ad]').contents().length) {
 var adType = $j(this).attr('data-adocean-id');
 $j('[data-showcase-id="'+adType+'"]').hide();
 $j(this).show();

 if (adType === 'c_top_300_250') {
 $j('#showCatAdvertOne').css('padding-bottom', '10px');
 }
 if (adType === 'c_bottom_300_250') {
 $j('#showCatAdvertTwo').css('padding-bottom', '10px');
 }
 if (adType === 'l_header_750_100' || adType === 'l_header_970_100' || adType === 'c_header_970_100' || adType === 'c_header_750_100' || adType === 'm_header_750_100' || adType === 'm_header_970_100') {
  var adoceanHeader = $j('#adoceanHeader');
 adoceanHeader.remove();
 $j('#wrapper').before(adoceanHeader);
 if ($j.browser.webkit) {
 $j('body').css('zoom', '100.00001%');
 }

 }
 if (adType === 'l_left_top_160_600' || adType === 'l_left_bottom_160_600') {
 $j('#isAdvert').show();
 }

 clearInterval(allAdocean.interval);
 }
 }
 );
 allAdocean.intervalCount++;
 if (allAdocean.intervalCount > 5) {
 clearInterval(allAdocean.interval);
 }
 },
 700
 )
 }
 }

 _cmParams.push({ path: "laptop"});




  ado.preview
({enabled: true,
emiter: "gg.adocean.pl"});


_adoCalls.push
({type: "master", params: {
id: "MTc80m713Q7UstlQBQWhvXr8XTOT58enUIv4_1KKHiT.N7"
, server: "gg.adocean.pl", keys: ["","laptop"]}});

  _adoCalls.push(
{
type: "slave",
slaveId: "adoceangglgmsmtqoxj",
params: {
myMaster: "MTc80m713Q7UstlQBQWhvXr8XTOT58enUIv4_1KKHiT.N7"
}});
  _adoCalls.push(
{
type: "slave",
slaveId: "adoceanggwahqcklrae",
params: {
myMaster: "MTc80m713Q7UstlQBQWhvXr8XTOT58enUIv4_1KKHiT.N7"
}});
  _adoCalls.push(
{
type: "slave",
slaveId: "adoceanggtboggxegud",
params: {
myMaster: "MTc80m713Q7UstlQBQWhvXr8XTOT58enUIv4_1KKHiT.N7"
}});
    _adoCalls.push({type: "afterCallback", callback: allAdocean.showAds});

 (function() {
 var cm = document.createElement('script'); cm.type = 'text/javascript'; cm.async = true;
 cm.src = 'http://adct.gg.pl/ct.js';
 var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(cm, s);
 })();



//]]>
</script> </body>
</html>'''

EXAMPLE_ERROR = '''\
<!DOCTYPE html>

<html class="no-js " xmlns="http://www.w3.org/1999/xhtml" xml:lang="pl" lang="pl" xmlns:fb="http://www.facebook.com/2008/fbml" xmlns:og="http://opengraphprotocol.org/schema/">
<head>
<meta charset="utf-8">
   <link rel="shortcut icon" href="http://static.allegrostatic.pl/site_images/1/0/common/favicon2.ico" />
   <link rel="apple-touch-icon" href="http://static.allegrostatic.pl/site_images/1/0/common/icon.jpg"/>

 <title>Niemaczegos - Allegro.pl - Więcej niż aukcje. Najlepsze oferty na największej platformie handlowej.</title>

  <meta name="keywords" content="aukcje internetowe,allegro,serwis aukcyjny" />
 <meta name="description" content="Allegro - najwięcej ofert w jednym miejscu. Radość zakupów i 100% bezpieczeństwa dla każdej transakcji. Kup Teraz!" />
 <meta name="classification" content="global,all" />
 <meta name="robots" content="all,index,follow" />
 <meta name="revisit-after" content="2 days" />


   <meta property="fb:admins" content="1683271640,658737674,638512944" />
  <meta property="fb:page_id" content="169267498107" />





  <link rel="stylesheet" media="screen" type="text/css" href="http://static.allegrostatic.pl/site_images/1/0/css/vela-pages-layout_av.2013.37.4.css" title="" /><link rel="stylesheet" media="print" type="text/css" href="http://static.allegrostatic.pl/site_images/1/0/css/print_av.2013.37.4.css" title="" /><link rel="alternate stylesheet" media="screen" type="text/css" href="http://static.allegrostatic.pl/site_images/1/0/css/print_preview_av.2013.37.4.css" title="Print Preview" /><link rel="stylesheet" media="screen" type="text/css" href="http://c.allegrostatic.pl/styles/vela-common.css?v=88ee4dfc133a763089ddfb1efd87f20c" title="" /><link rel="stylesheet" media="screen" type="text/css" href="http://static.allegrostatic.pl/site_images/1/0/css/vela-layout_av.2013.37.4.css" title="" />

   <link href="https://plus.google.com/100042465934078110473" rel="publisher" />

 <script src="http://static.allegrostatic.pl/js/libs/modernizr-2.6.2.min-3.js"></script>


 <script type="text/javascript" src="//gg.adocean.pl/files/js/ado.js"></script>
 <script type="text/javascript">
 if(typeof ado!=="object"){ado={};ado.config=ado.preview=ado.placement=ado.master=ado.slave=function(){};}
 ado.config({mode: "new", xml: false, characterEncoding: true});
 ado.preview({enabled: true, emiter: "gg.adocean.pl", id: "JOcK7gzdoyrcIT2176iLzhCz8UoPOGcT6Y1ax8FNTPf.l7"});
 ado.master({id: 'OccHlQDANw9IvVa1bbZo9d2Hf7N2rm9aXjdx80etjun.a7', server: 'gg.adocean.pl' });
 </script>


<script type="text/javacript">
// <![CDATA[
 var gomez={
 gs: new Date().getTime(),
 acctId:'B3A70B',
 pgId:'listing',
 grpId:'1',
 wrate:0.01
 };
// ]]>
</script>

<script type="text/javascript">var header=1;</script>
<!-- acmHeader-->

<script type="text/javascript">
 (function() {
 var opti = document.createElement('script'); opti.type = 'text/javascript'; opti.async = true;
 opti.src = '//cdn.optimizely.com/js/70910669.js';
 var s = document.getElementsByTagName('head')[0]; s.appendChild(opti);
 })();
</script>


  <script type="text/javascript">

 var _gaq = _gaq || [];
 var trackers = new Array();


  trackers.push('t0');

 _gaq.push(['t0._setAccount', 'UA-2827377-1']);
   _gaq.push(['t0._setSampleRate', '1']);
    _gaq.push(['t0._setDomainName', '.allegro.pl']);


 _gaq.push(['t0._trackPageview']);




 (function() { var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true; ga.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'stats.g.doubleclick.net/dc.js'; var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s); })();

  </script>

</head>

<!--[if lte IE 8]><body class="ie8 allegro-pl       " data-country-code="1"><![endif]-->
<!--[if gt IE 8]><!--><body class="allegro-pl       " data-country-code="1"><!--<![endif]-->

<!-- Google Tag Manager -->
<noscript><iframe src="//www.googletagmanager.com/ns.html?id=GTM-FXVJ"
 height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
 new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
 j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
 '//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-FXVJ');</script>
<!-- End Google Tag Manager -->


 <input type="hidden" id="cookie-policy-banner-config" data-config='{"url":"http://allegro.pl/country_pages/1/0/cookie_policy.php","langs":{"message":"Strona korzysta z plików cookies w celu realizacji usług i zgodnie z %link%. Możesz określić warunki przechowywania lub dostępu do plików cookies w Twojej przeglądarce.","anchor":"Polityką Plików Cookies"}}'>






<div id="wrapper">
 <div class="vela">
 <!-- MAIN HEADER -->
 <div class="main-header clearfix" id="main-header">

 <!-- USER NAV -->
 <ul class="user-nav">

 <li class="ma-layer">
 <a class="alle-link" href="http://allegro.pl/myaccount/">
 <span>moje allegro</span>
 <i></i>
 </a>
  <ul id="ma-layer">
  <li>
 <a href="http://allegro.pl/myaccount/won.php">
 <span>kupione</span>
 </a>
 </li>
  <li>
 <a href="http://allegro.pl/myaccount/watch.php">
 <span>obserwowane</span>
 </a>
 </li>
  <li>
 <a href="http://allegro.pl/myaccount/bid.php">
 <span>licytujesz</span>
 </a>
 </li>
  <li>
 <a href="http://allegro.pl/NewItem/">
 <span>wystaw przedmiot</span>
 </a>
 </li>
  <li>
 <a href="http://allegro.pl/myaccount/sell.php">
 <span>sprzedajesz</span>
 </a>
 </li>
  <li>
 <a href="http://allegro.pl/myaccount/sold.php">
 <span>sprzedane</span>
 </a>
 </li>
  <li>
 <a href="http://allegro.pl/myaccount/feedbacks/add.php">
 <span>wystaw komentarz</span>
 </a>
 </li>
  <li>
 <a href="http://allegro.pl/myaccount/feedbacks/feedbacks.php">
 <span>komentarze otrzymane</span>
 </a>
 </li>
  </ul>


 <li class="register">
 <a href="http://allegro.pl/Register.php"><span>zarejestruj</span></a>
 </li>

 <li class="login">
 <a href="https://ssl.allegro.pl/fnd/authentication/"><span>zaloguj</span></a>
 </li>


 </ul>
 <!-- / END USER NAV -->


 <!-- SEARCH BAR -->
 <div class="search-bar" id="search-bar">
 <div class="in clearfix">
 <h2 class="logo">
 <a href="http://allegro.pl/" title="Allegro.pl - aukcje internetowe, bezpieczne zakupy">
 <img src="http://static.allegrostatic.pl/site_images/1/0/vela/allegro-logo.png" alt="Allegro.pl - aukcje internetowe, bezpieczne zakupy" width="174" height="59">
 </a>
 </h2>

  <div class="common">
 <form action="http://allegro.pl/listing.php/search" method="get" class="main-search" id="main-search"
 data-actions='{"default":{"action":"\/listing.php\/search","param":"string"},"shop":{"action":"\/shop.php\/Listing","param":"shopName"},"user":{"action":"\/show_user.php","param":"search"},"shopItems":{"action":"\/shop.php\/Show","param":"string"},"userItems":{"action":"\/listing\/user.php","param":"string"}}'
 data-base-url='http://allegro.pl' data-cookie-domain=''>

 <div class="input-text-wrapper">
 <input id="main-search-text" placeholder="czego szukasz?"
 type="text" required="required" name="string"
 value="niemaczegos" x-webkit-speech autocomplete="off">
 </div>

  <select name="search_scope" class="search-type-select">
 <option value="">wszystkie działy</option>
  <option value="electronics">
 Elektronika </option>
  <option value="fashion.beauty">
 Moda i uroda </option>
  <option value="household.health">
 Dom i zdrowie </option>
  <option value="baby">
 Dziecko </option>
  <option value="culture.entertainment">
 Kultura i rozrywka </option>
  <option value="sports.leisure">
 Sport i wypoczynek </option>
  <option value="automotive">
 Motoryzacja </option>
  <option value="collections.art">
 Kolekcje i sztuka </option>
  <option value="company.services">
 Firma i usługi </option>


  <option value="shop">
 sklepy </option>
  <option value="user">
 użytkownicy </option>
  <option value="closed">
 zakończone </option>
  <option class="custom-search-type"></option>
 </select>

 <input type="submit" class="sprite search-btn" value="Szukaj">

  <div class="search-type-select">
 <ul>
 <li><a class="active" href="#">wszystkie działy</a></li>
  <li><a href="#electronics">Elektronika</a></li>
  <li><a href="#fashion.beauty">Moda i uroda</a></li>
  <li><a href="#household.health">Dom i zdrowie</a></li>
  <li><a href="#baby">Dziecko</a></li>
  <li><a href="#culture.entertainment">Kultura i rozrywka</a></li>
  <li><a href="#sports.leisure">Sport i wypoczynek</a></li>
  <li><a href="#automotive">Motoryzacja</a></li>
  <li><a href="#collections.art">Kolekcje i sztuka</a></li>
  <li><a href="#company.services">Firma i usługi</a></li>


  <li class="separator-top">
 <a href="#shop">sklepy</a>
 </li>
  <li>
 <a href="#user">użytkownicy</a>
 </li>
  <li>
 <a href="#closed">zakończone</a>
 </li>
  </ul>
 <strong title="">
  <span>wszystkie działy</span>
  <i class="sprite"></i>
 </strong>
 </div>

 <div class="search-layer">
 <div class="auto-complete-list"></div>
 <label class="in-description">
 <input tabindex="2" type="checkbox" value="1" name="description"> Szukaj też w opisach i parametrach </label>
 </div>

 <script type="text/template" id="default-suggestion-tpl">
 <li data-type="1">
 <span class="phrase"><%= phrase %></span>
 </li>
 </script>

 <script type="text/template" id="in-category-suggestion-tpl">
 <li data-type="2" data-category="<%= category_id %>">
 <span class="phrase"><%= phrase %></span>
 <em>w kategorii <b><%= category %></b></em>
 </li>
 </script>

 <script type="text/template" id="in-history-suggestion-tpl">

 <li data-type="1">
 <a class="remove" href="#" data-id="<%= id %>"><span>usuń</span></a><span class="phrase"><%= phrase %></span>
 </li>

 </script>

 </form>
 </div>

  <div class="cart-status empty">
 <p class="price">
  koszyk jest pusty  </p>
 <p class="count">
 <a href="http://allegro.pl/Cart.php" class="sprite">
 <span></span>
 </a>
 </p>
 </div>
 <a class="toggle-trigger" href="#toggle-trigger" data-lang="">
 <i class="sprite"></i><span class="sprite"></span>
 </a>
  </div>
     </div>
 <!-- /END SEARCH BAR -->

 </div>
 <!-- /END MAIN HEADER -->

 <!-- DEPARTMENTS -->
  <div class="main-nav clearfix" id="main-nav" data-url-root="http://allegro.pl/dzial/layer">
    <ul>
                        <li class="nav-tab">
        <a class="nav-link" href="http://allegro.pl/dzial/elektronika">
            <strong>Elektronika</strong>
        </a>
        <div class="layer-wrapper">
            <div class="layer" data-department="electronics"></div>
        </div>
    </li>

                        <li class="nav-tab">
        <a class="nav-link" href="http://allegro.pl/dzial/moda-i-uroda">
            <strong>Moda <span>i uroda</span></strong>
        </a>
        <div class="layer-wrapper">
            <div class="layer" data-department="fashion.beauty"></div>
        </div>
    </li>

                        <li class="nav-tab">
        <a class="nav-link" href="http://allegro.pl/dzial/dom-i-zdrowie">
            <strong>Dom <span>i zdrowie</span></strong>
        </a>
        <div class="layer-wrapper">
            <div class="layer" data-department="household.health"></div>
        </div>
    </li>

                        <li class="nav-tab">
        <a class="nav-link" href="http://allegro.pl/dzial/dziecko">
            <strong>Dziecko</strong>
        </a>
        <div class="layer-wrapper">
            <div class="layer" data-department="baby"></div>
        </div>
    </li>

                        <li class="nav-tab">
        <a class="nav-link" href="http://allegro.pl/dzial/kultura-i-rozrywka">
            <strong>Kultura <span>i rozrywka</span></strong>
        </a>
        <div class="layer-wrapper">
            <div class="layer" data-department="culture.entertainment"></div>
        </div>
    </li>

                        <li class="nav-tab">
        <a class="nav-link" href="http://allegro.pl/dzial/sport-i-wypoczynek">
            <strong>Sport <span>i wypoczynek</span></strong>
        </a>
        <div class="layer-wrapper">
            <div class="layer" data-department="sports.leisure"></div>
        </div>
    </li>

                        <li class="nav-tab">
        <a class="nav-link" href="http://allegro.pl/dzial/motoryzacja">
            <strong>Motoryzacja</strong>
        </a>
        <div class="layer-wrapper">
            <div class="layer" data-department="automotive"></div>
        </div>
    </li>

                        <li class="nav-tab">
        <a class="nav-link" href="http://allegro.pl/dzial/kolekcje-i-sztuka">
            <strong>Kolekcje <span>i sztuka</span></strong>
        </a>
        <div class="layer-wrapper">
            <div class="layer" data-department="collections.art"></div>
        </div>
    </li>

                        <li class="nav-tab">
        <a class="nav-link" href="http://allegro.pl/dzial/firma-i-uslugi">
            <strong>Firma <span>i usługi</span></strong>
        </a>
        <div class="layer-wrapper">
            <div class="layer" data-department="company.services"></div>
        </div>
    </li>

                    <li class="nav-tab last-child">
        <a class="nav-link" href="http://allegro.pl/dzial/strefa-okazji">
            <strong>Strefa <span>okazji</span></strong>
        </a>
        <div class="layer-wrapper">
            <div class="layer" data-department="other"></div>
        </div>
    </li>

    </ul>
</div>

  <!-- END DEPARTMENTS -->

 <!-- BREADCRUMBS -->
  <div class="main-breadcrumb separator-bottom   search">
 <div class="main-functional-button">
  <div class="btn-group" role="listbox">
  <button class="btn" type="button" role="option" id="add-search-to-favourites" onClick="location.href='/myaccount/favourites/favourites_search.php/addNew/?change_view=Poka%C5%BC&endingTime=7&offerTypeBuyNow=1&standard_allegro=1&string=niemaczegos'">
 dodaj do ulubionych zapytań </button>
  <button class="btn dropdown-toggle" type="button" role="option" data-toggle="dropdown">
 <span class="carret"></span>
 </button>
 <ul class="dropdown-menu menu-to-right" role="option">
  <li><a id="rss-feed-search" href="/rss.php?feed=search&change_view=Poka%C5%BC&endingTime=7&offerTypeBuyNow=1&standard_allegro=1&string=niemaczegos"
 >dodaj kanał RSS </a></li>
  </ul>
  </div>
  </div>
 <div class="main-title-breadcrumbs clearfix">
 <div class="main-title">
 <h1>szukasz <span>niemaczegos</span></h1>
<small id="main-breadcrumb-search-hits">(0 ofert)</small>
 </div>
  <ul class="main-breadcrumb-list clearfix" id="breadcrumbs-list">
 <li>
 <a href="http://allegro.pl"><span>Allegro</span></a>
 </li>

  <li>Wyniki wyszukiwania</li> </ul>
 </div>
 </div>
  <!-- END BREADCRUMBS -->

</div>


  <div id="pagecontent1" class="main-content clearfix">









 <div id="sidebar" class="sidebar">
 <section class="widget" id="sidebar-categories" data-current-category-id="" data-current-category-name="">
 <div class="widget-header" data-helptip-body='' data-helptip-uri="true"
 >
 <h2>Podkategorie</h2>
    </div>
 <div class="widget-content">
 <nav class="widget-nav">
 <ul>
    <li id="sidebar-cat-0" class="sidebar-cat current parent-empty"><span class="name">Allegro</span><span class="count"> (0)</span></li>
     <li id="sidebar-cat-26013" class="sidebar-cat  empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=26013&offerTypeBuyNow=1&standard_allegro=1&string=niemaczegos">
 <span class="name"><span>Antyki i Sztuka</span></span>
 </a>
 <span class="count">()</span>
  </li>
    <li id="sidebar-cat-98553" class="sidebar-cat  empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=98553&offerTypeBuyNow=1&standard_allegro=1&string=niemaczegos">
 <span class="name"><span>Bilety</span></span>
 </a>
 <span class="count">()</span>
  </li>
    <li id="sidebar-cat-64477" class="sidebar-cat  empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=64477&offerTypeBuyNow=1&standard_allegro=1&string=niemaczegos">
 <span class="name"><span>Biuro i Reklama</span></span>
 </a>
 <span class="count">()</span>
  </li>
    <li id="sidebar-cat-19732" class="sidebar-cat  empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=19732&offerTypeBuyNow=1&standard_allegro=1&string=niemaczegos">
 <span class="name"><span>Biżuteria i Zegarki</span></span>
 </a>
 <span class="count">()</span>
  </li>
    <li id="sidebar-cat-73973" class="sidebar-cat  empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=73973&offerTypeBuyNow=1&standard_allegro=1&string=niemaczegos">
 <span class="name"><span>Delikatesy</span></span>
 </a>
 <span class="count">()</span>
  </li>
    <li id="sidebar-cat-11763" class="sidebar-cat  empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=11763&offerTypeBuyNow=1&standard_allegro=1&string=niemaczegos">
 <span class="name"><span>Dla Dzieci</span></span>
 </a>
 <span class="count">()</span>
  </li>
    <li id="sidebar-cat-5" class="sidebar-cat  empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=5&offerTypeBuyNow=1&standard_allegro=1&string=niemaczegos">
 <span class="name"><span>Dom i Ogród</span></span>
 </a>
 <span class="count">()</span>
  </li>
    <li id="sidebar-cat-63757" class="sidebar-cat  empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=63757&offerTypeBuyNow=1&standard_allegro=1&string=niemaczegos">
 <span class="name"><span>Erotyka</span></span>
 </a>
 <span class="count">()</span>
  </li>
    <li id="sidebar-cat-20585" class="sidebar-cat  empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=20585&offerTypeBuyNow=1&standard_allegro=1&string=niemaczegos">
 <span class="name"><span>Filmy</span></span>
 </a>
 <span class="count">()</span>
  </li>
    <li id="sidebar-cat-8845" class="sidebar-cat  empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=8845&offerTypeBuyNow=1&standard_allegro=1&string=niemaczegos">
 <span class="name"><span>Fotografia</span></span>
 </a>
 <span class="count">()</span>
  </li>
    <li id="sidebar-cat-9" class="sidebar-cat  empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=9&offerTypeBuyNow=1&standard_allegro=1&string=niemaczegos">
 <span class="name"><span>Gry</span></span>
 </a>
 <span class="count">()</span>
  </li>
    <li id="sidebar-cat-122640" class="sidebar-cat  empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=122640&offerTypeBuyNow=1&standard_allegro=1&string=niemaczegos">
 <span class="name"><span>Instrumenty</span></span>
 </a>
 <span class="count">()</span>
  </li>
    <li id="sidebar-cat-6" class="sidebar-cat  empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=6&offerTypeBuyNow=1&standard_allegro=1&string=niemaczegos">
 <span class="name"><span>Kolekcje</span></span>
 </a>
 <span class="count">()</span>
  </li>
    <li id="sidebar-cat-2" class="sidebar-cat  empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=2&offerTypeBuyNow=1&standard_allegro=1&string=niemaczegos">
 <span class="name"><span>Komputery</span></span>
 </a>
 <span class="count">()</span>
  </li>
    <li id="sidebar-cat-122233" class="sidebar-cat  empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=122233&offerTypeBuyNow=1&standard_allegro=1&string=niemaczegos">
 <span class="name"><span>Konsole i automaty</span></span>
 </a>
 <span class="count">()</span>
  </li>
    <li id="sidebar-cat-7" class="sidebar-cat  empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=7&offerTypeBuyNow=1&standard_allegro=1&string=niemaczegos">
 <span class="name"><span>Książki i Komiksy</span></span>
 </a>
 <span class="count">()</span>
  </li>
    <li id="sidebar-cat-3" class="sidebar-cat  empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=3&offerTypeBuyNow=1&standard_allegro=1&string=niemaczegos">
 <span class="name"><span>Motoryzacja</span></span>
 </a>
 <span class="count">()</span>
  </li>
    <li id="sidebar-cat-1" class="sidebar-cat  empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=1&offerTypeBuyNow=1&standard_allegro=1&string=niemaczegos">
 <span class="name"><span>Muzyka</span></span>
 </a>
 <span class="count">()</span>
  </li>
    <li id="sidebar-cat-20782" class="sidebar-cat  empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=20782&offerTypeBuyNow=1&standard_allegro=1&string=niemaczegos">
 <span class="name"><span>Nieruchomości</span></span>
 </a>
 <span class="count">()</span>
  </li>
    <li id="sidebar-cat-1454" class="sidebar-cat  empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=1454&offerTypeBuyNow=1&standard_allegro=1&string=niemaczegos">
 <span class="name"><span>Odzież, Obuwie, Dodatki</span></span>
 </a>
 <span class="count">()</span>
  </li>
    <li id="sidebar-cat-16696" class="sidebar-cat  empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=16696&offerTypeBuyNow=1&standard_allegro=1&string=niemaczegos">
 <span class="name"><span>Przemysł</span></span>
 </a>
 <span class="count">()</span>
  </li>
    <li id="sidebar-cat-76593" class="sidebar-cat  empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=76593&offerTypeBuyNow=1&standard_allegro=1&string=niemaczegos">
 <span class="name"><span>Rękodzieło</span></span>
 </a>
 <span class="count">()</span>
  </li>
    <li id="sidebar-cat-10" class="sidebar-cat  empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=10&offerTypeBuyNow=1&standard_allegro=1&string=niemaczegos">
 <span class="name"><span>RTV i AGD</span></span>
 </a>
 <span class="count">()</span>
  </li>
    <li id="sidebar-cat-3919" class="sidebar-cat  empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=3919&offerTypeBuyNow=1&standard_allegro=1&string=niemaczegos">
 <span class="name"><span>Sport i Turystyka</span></span>
 </a>
 <span class="count">()</span>
  </li>
    <li id="sidebar-cat-122332" class="sidebar-cat  empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=122332&offerTypeBuyNow=1&standard_allegro=1&string=niemaczegos">
 <span class="name"><span>Sprzęt estradowy, studyjny i DJ-ski</span></span>
 </a>
 <span class="count">()</span>
  </li>
    <li id="sidebar-cat-4" class="sidebar-cat  empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=4&offerTypeBuyNow=1&standard_allegro=1&string=niemaczegos">
 <span class="name"><span>Telefony i Akcesoria</span></span>
 </a>
 <span class="count">()</span>
  </li>
    <li id="sidebar-cat-1429" class="sidebar-cat  empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=1429&offerTypeBuyNow=1&standard_allegro=1&string=niemaczegos">
 <span class="name"><span>Uroda</span></span>
 </a>
 <span class="count">()</span>
  </li>
    <li id="sidebar-cat-105411" class="sidebar-cat  empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=105411&offerTypeBuyNow=1&standard_allegro=1&string=niemaczegos">
 <span class="name"><span>Usługi</span></span>
 </a>
 <span class="count">()</span>
  </li>
    <li id="sidebar-cat-55067" class="sidebar-cat  empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=55067&offerTypeBuyNow=1&standard_allegro=1&string=niemaczegos">
 <span class="name"><span>Wakacje</span></span>
 </a>
 <span class="count">()</span>
  </li>
    <li id="sidebar-cat-121882" class="sidebar-cat  empty">
  <a href="/listing/listing.php?change_view=Poka%C5%BC&endingTime=7&id=121882&offerTypeBuyNow=1&standard_allegro=1&string=niemaczegos">
 <span class="name"><span>Zdrowie</span></span>
 </a>
 <span class="count">()</span>
  </li>
    </ul>
 </nav>
 </div>
</section>
 <section id="sidebar-params" class="widget widget-params widget-params-live">
 <div class="widget-header">
 <h2 class="headerBar">Parametry</h2>
 <a class="action action-reset" href="#"><span>Wyczyść</span></a>
 </div>
 <div class="widget-content">
 <input type="hidden" class="jslangs" data-no-param-found="Nie znaleziono parametru." data-search-other="znajdź inne" data-choose="Wybierz" />
 <form action="/listing/listing.php" method="get" name="display-form" id="display-form" data-token="1a1d593193ebe7558884125529bf5631" >
  <input type="hidden" name="string" value="niemaczegos" />


   <fieldset>
 <h3>Stan</h3>
 <ul>
 <li>
 <input name="buyNew" type="checkbox" id="offerBuy4" value="1" />
 <label for="offerBuy4" class="disabled">Nowe <span class="count count-disabled">(0)</span></label>
 </li>
 <li>
 <input name="buyUsed" type="checkbox" id="offerBuy5" value="1" />
 <label for="offerBuy5" class="disabled">Używane <span class="count count-disabled">(0)</span></label>
 </li>
 </ul>
 </fieldset>
   <fieldset>
 <h3>Rodzaj oferty</h3>
 <ul>
   <li>
 <input name="offerTypeBuyNow" type="checkbox" id="buyNowParam" value="1" />
 <label for="buyNowParam" class="disabled">Kup Teraz <span class="count count-disabled">(0)</span></label>
 </li>
       <li>
 <input name="offerTypeAuction" type="checkbox" id="auctionsParam" value="2" />
 <label for="auctionsParam" class="disabled">Licytacje <span class="count count-disabled">(0)</span></label>
 </li>
        </ul>
 </fieldset>

  <fieldset>
 <h3>Cena (zł)</h3>
 <ul class="param-price-range">
 <li class="param-type-range param-type-placeholder">
 <input type="checkbox" value="1" name="price_enabled" />
 <label for="price_from"><span>od</span></label>
 <input type="text" name="price_from" id="price_from" data-validate-anchor="priceFrom" data-error-style="tooltip" placeholder="od" value="" size="5" />&ndash;
 <label for="price_to"><span>do</span></label>
 <input type="text" name="price_to" id="price_to" data-validate-anchor="priceTo" data-error-style="tooltip" placeholder="do" value="" size="5" />
 </li>
 </ul>
 </fieldset>

   <fieldset>
 <h3>Lokalizacja</h3>
 <ul>
 <li class="param-type-placeholder">
 <input id="locationRadio3" type="radio" name="postcode_enabled" value="2" />
 <label for="city_id">miejscowość:</label>
 <input type="text" name="city" id="city_id" size="10" placeholder="miejscowość" value="" />
 </li>
 <li class="param-type-placeholder param-distance-state">
 <input id="locationRadio1" type="radio" name="postcode_enabled" value="0" checked="checked" />
 <select name="state" id="state" placeholder="województwo">
 <option value="" class="disabled">województwo</option>
 <option value="1">z dolnośląskiego</option><option value="2">z kujawsko-pomorskiego</option><option value="3">z lubelskiego</option><option value="4">z lubuskiego</option><option value="5">z łódzkiego</option><option value="6">z małopolskiego</option><option value="7">z mazowieckiego</option><option value="8">z opolskiego</option><option value="9">z podkarpackiego</option><option value="10">z podlaskiego</option><option value="11">z pomorskiego</option><option value="12">ze śląskiego</option><option value="13">ze świętokrzyskiego</option><option value="14">z warmińsko-mazurskiego</option><option value="15">z wielkopolskiego</option><option value="16">z zachodniopomorskiego</option> </select>
 </li>
  <li class="param-type-placeholder param-distance-postcode">
 <input type="radio" id="locationRadio2" name="postcode_enabled" value="1" />
 <label for="postcode_enabled">w odległości do:</label>
 <select name="distance" class="cLabel" placeholder="km" data-dependent='["postcode"]'>
 <option value="" class="disabled">km</option>
 <option value="1">10</option><option value="2">25</option><option value="3">50</option><option value="4">75</option><option value="5">100</option><option value="6">150</option><option value="7">200</option><option value="8">350</option><option value="9">500</option> </select>
 <span>od</span>
 <label for="distanceFromPostcodeInput"><span>kod</span></label>
 <input type="text" name="postcode" id="distanceFromPostcodeInput" size="6" maxlength="6" placeholder="kod" data-dependent='["distance"]' data-validate-anchor="postcode" data-error-style="tooltip"  />
 </li>
  </ul>
 </fieldset>

 <div class="">

 <div id="moreParamsBlock">
  </div>
  </div><!-- /catAttribBlock -->

 <fieldset>
 <h3>oferta ma</h3>
 <ul class="no-scroll">
  <li>
 <input type="checkbox" name="standard_allegro" id="standard_allegro1" value="1" checked="checked" />
 <label for="standard_allegro1">Standard Allegro <i class="icon-as"></i></label>
 </li>
   <li>
 <input id="freeShipping" type="checkbox" name="freeShipping" value="1" />
 <label for="freeShipping">wysyłka GRATIS <i class="icon-fs"></i></label>
 </li>
    <li>
 <input id="installmentAvailable" type="checkbox" name="installmentAvailable" value="1" data-helptip-body="Dodaliśmy filtr <em>Raty PayU</em>. Zaznacz go, jeśli chcesz zobaczyć tylko oferty, za które możesz zapłacić w ratach." >
 <label for="installmentAvailable">Raty <span class="specialcase">PayU</span> <i class="icon-pi"></i></label>
 </li>

  <li>
 <input id="personal_id" type="checkbox" name="personal_rec" value="1" />
 <label for="personal_id">Odbiór osobisty</label>
 </li>


  <li>
 <input id="vat_id" type="checkbox" name="vat_invoice" value="1" />
 <label for="vat_id">Faktura <span class="specialcase">VAT</span> <!-- <span class="count">()</span> --></label>
 </li>

  <li>
 <input id="generalDelivery_id" type="checkbox" name="generalDelivery_rec" value="1" />
 <label for="generalDelivery_id">Odbiór w punkcie</label>
 </li>

   </ul>
 </fieldset>

   <fieldset>
 <h3>Czas realizacji</h3>
 <ul>
 <li class="param-type-placeholder param-shipping-time">
 <input type="checkbox" name="shippingTime_enabled" value="1" />
 <select id="shippingTime" name="shippingTime" placeholder="czas">
 <option value="" class="disabled">czas</option>
  <option id="shippingTime_24" value="24">24 godziny</option>
  <option id="shippingTime_48" value="48">do 2 dni</option>
  <option id="shippingTime_72" value="72">do 3 dni</option>
  <option id="shippingTime_96" value="96">do 4 dni</option>
  <option id="shippingTime_120" value="120">do 5 dni</option>
  <option id="shippingTime_168" value="168">do 7 dni</option>
  <option id="shippingTime_240" value="240">do 10 dni</option>
  <option id="shippingTime_336" value="336">do 14 dni</option>
  <option id="shippingTime_504" value="504">do 21 dni</option>
  <option id="shippingTime_999" value="999">dłużej</option>
  </select>
 </li>
 </ul>
 </fieldset>

 <fieldset>
 <h3>wystawione</h3>
 <ul>
 <li class="param-type-placeholder">
 <input type="checkbox" name="startingTime_enabled" value="1" />
 <span>w ciągu</span>
 <select name="startingTime" id="startingTime_id" placeholder="czas">
 <option value="" class="disabled">czas</option>
 <option value="1">1 godziny</option><option value="2">2 godzin</option><option value="3">3 godzin</option><option value="4">4 godzin</option><option value="5">5 godzin</option><option value="6">12 godzin</option><option value="7" selected="selected">24 godzin</option><option value="8">2 dni</option><option value="9">3 dni</option><option value="10">4 dni</option><option value="11">5 dni</option><option value="12">6 dni</option><option value="13">7 dni</option> </select>
 </li>
 </ul>
 </fieldset>

 <fieldset>
 <h3>kończące się</h3>
 <ul>
 <li class="param-type-placeholder">
 <input type="checkbox" name="endingTime_enabled" value="1" />
 <span>w ciągu</span>
 <select name="endingTime" id="endingTime_id" placeholder="czas">
 <option value="" class="disabled">czas</option>
 <option value="1">1 godziny</option><option value="2">2 godzin</option><option value="3">3 godzin</option><option value="4">4 godzin</option><option value="5">5 godzin</option><option value="6">12 godzin</option><option value="7" selected="selected">24 godzin</option><option value="8">2 dni</option><option value="9">3 dni</option><option value="10">4 dni</option><option value="11">5 dni</option><option value="12">6 dni</option><option value="13">7 dni</option> </select>
 </li>
 </ul>
 </fieldset>


 <div class="clearfix"></div>
 <fieldset class="submit">
 <div class="button-wrapper">
 <input type="submit" class="btn" value="Pokaż" name="change_view" />
 </div>
 </fieldset>
  </form>
 </div>
 <script id="sidebar-params-validation-rules" type="js/data">

 {
 "postcode":[{"required":false},{"pattern":"postcodePL","msg":"Niewłaściwy sposób zapisu"},{"minLength":4,"msg":"Zbyt krótki wpis"},{"maxLength":12,"msg":"Zbyt długi wpis"}],
 "priceFrom":[{"required":false},{"pattern":"amountPL","msg":"Niewłaściwy sposób zapisu"}],
 "priceTo":[{"required":false},{"pattern":"amountPL","msg":"Niewłaściwy sposób zapisu"}]
 }

 </script>
 <script id="sidebar-params-validation-samples" type="js/data">
 {"postcode":"00-000"}
 </script>
</section><!-- /sidebar-params -->

<script id="sidebar-params-toggle-link" type="text/template">
 <a href="#" class="toggle expanded">
 <span class="label-collapse"><span class="arrow">&lt;</span> <span>mniej</span></span>
 <span class="label-expand"><span>więcej</span> <span class="arrow">&gt;</span></span>
 </a>
</script>




  <section id="sidebar-adocean" class="widget widget-adverts widget-adocean">
 <div class="widget-content">
 <div data-adocean-id="l_left_top_160_600" style="display: none;"><div id="adoceanggwahqcklrae" data-ad="1"></div></div> <div data-adocean-id="l_left_bottom_160_600" style="display: none;"><div id="adoceanggtboggxegud" data-ad="1"></div></div> </div>
 </section>
 </div>
<div id="listing" class="listing " data-is-live-search-active="1" data-popup='{"token":"1a1d593193ebe7558884125529bf5631","cartid":""}' data-txt='{"samplePhoto":"zdjęcie poglądowe","loading":"Ładowanie"}' data-catcounters='[]' data-totalcounter='0 ofert'  data-headtitle="Niemaczegos - Allegro.pl - Więcej niż aukcje. Najlepsze oferty na największej platformie handlowej.">


  <div class="listing-message">
 <p class="main-message">Nasze oferty nie sprostały Twoim wymaganiom.</p>
  <p class="sub-message">Może zrezygnujesz z niektórych parametrów?</p>
 </div>  <div class="listing-options-bottom">
  </div>
</div>

<section id="listing-message-modal" class="modal listing-message-modal hide fade">
 <div class="modal-header">
 <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
 <h3></h3>
 </div>
 <div class="modal-body"></div>
</section>

<a id="go-to-top" class="go-to-top hidden" href="#"></a>

 <div class="recommended-listing">
 <div class="vela">
 <section class="recommended items-box carousel-box loading" id="items-carousel-recommended" data-url='http://recommend.allegro.pl/?sId[0]=16&caLvl1=0&caLvl2=0&caLvl3=0&caLvl4=0&uId=&uHash=Na2e8746e2013fa88a2864a9646a50846'>
 <h2>otwórz się na <span>inne pomysły</span></h2>

 <div class="items-carousel">
 <div class="carousel-nav">
 <a class="sprite carousel-prev" title="Poprzednia strona" href="#carousel-prev">
 Poprzednia strona </a>
 <a class="sprite carousel-next" title="Następna strona" href="#carousel-next">
 Następna strona </a>
 </div>
 <ul class="items-wrap"></ul>
 </div>
 </section>
</div> </div>
 <script id="items-carousel-template-recommended" type="text/template">

 <li>
 <a href="/ShowItem2.php?item=<%= itemId %>&ars_source=ars&ars_socket_id=<%= socketId %>&ars_rule_id=<%= ruleId %>" title="<%= itemName %>" class="photo">
 <% if (photoLink) { %>
 <img src="<%= photoLink %>" width="128" height="96" alt="<%= itemName %>">
 <% } else { %>
 <span class="no-photo"></span>
 <% } %>
 </a>
 <% if (standard) { %><i class="icon-as"></i><% } %>
 <h3><a href="/ShowItem2.php?item=<%= itemId %>&ars_source=ars&ars_socket_id=<%= socketId %>&ars_rule_id=<%= ruleId %>"><span><%= itemName %></span></a></h3>

 <span class="price">
 <% if (buyNowPrice != 0) { %>
 <span class="buy-now">Kup Teraz</span><%= utils.formatPrice(buyNowPrice, priceFormat) %>
 <% } else { %>
 od <%= utils.formatPrice(bidPrice, priceFormat)%>
 <% } %>
 <% if (freeShipping) { %>
 <i class="icon-fs"></i>
 <% } %>
 </span>
 </li>

</script>

<script id="listing-icon-info" type="text/template">
{
 "standardAllegro": "<a href=\"http:\/\/uslugi.allegro.pl\/sa\/\" target=\"_blank\">Standard Allegro<\/a> to gwarancja udanej transakcji. Oznacza najwy\u017csz\u0105 jako\u015b\u0107 obs\u0142ugi klienta. O wyr\u00f3\u017cnieniu oferty w ten spos\u00f3b decyduj\u0105 nasze okre\u015blone kryteria oraz opinie kupuj\u0105cych.",
 "freeShipping": "<a href=\"http:\/\/uslugi.allegro.pl\/wg\/\" target=\"_blank\">Wysy\u0142ka Gratis<\/a> to co najmniej jedna darmowa opcja dostawy. W ten spos\u00f3b wygodniej dokonasz transakcji. Bez dodatkowych koszt\u00f3w!",
 "loyaltyProgram": ""}
</script>

<!-- saddr: 104-43-->
<!-- site: 1/0 -->


<!-- Footer start -->
 </div> <!-- /pagecontent1 -->

 <div class="vela">
 <div class="main-footer">
 <div class="clearfix">
 <p class="main-footer-logo">
 <a href="http://allegro.pl/">
 <img title="Allegro.pl - Więcej niż aukcje. Najlepsze oferty na największej platformie handlowej." src="http://static.allegrostatic.pl/site_images/1/0/vela/allegro-logo-small.png" width="67" width="23" alt="allegro">
 </a>
 </p>

 <ul class="main-footer-shortcuts">
  <li>
 <a class="" href="http://cafe.allegro.pl/">Cafe</a>
 </li>
  <li>
 <a class="" href="http://allegro.pl/country_pages/1/0/marketing/about.php">O nas</a>
 </li>
  <li>
 <a class="" href="http://kariera.allegro.pl/">Praca</a>
 </li>
  <li>
 <a class="" href="http://poznaj.allegro.pl/">Poznaj Allegro</a>
 </li>
  <li>
 <a class="" href="http://allegro.pl/country_pages/1/0/user_agreement.php">Regulamin</a>
 </li>
  <li>
 <a class=" open-help" href="javascript:OpenHelp()">Pomoc</a>
 </li>
  <li>
 <a class="" href="http://m.allegro.pl/">Wersja Mobilna</a>
 </li>
  </ul>
 </div>
 </div>
</div>



<p class="reg">
  Korzystanie z serwisu oznacza akceptację  <a href="http://allegro.pl/country_pages/1/0/user_agreement.php" class="alleLink"><span>regulaminu</span></a>
 <br /><a href="http://allegro.pl/country_pages/1/0/cookie_policy.php" class="alleLink"><span>Informacja o cookies</span></a>
</p>

 </div><!-- /footerContentBox -->

<script type="text/javascript">
<!--//--><![CDATA[//><!--
var gemius_identifier = new String('0iTgIucYowHxbRZHgZUtHeUUP_fFZCMccPZmta45O.b.87');
//--><!]]>
</script>
<script type="text/javascript" src="http://static.allegrostatic.pl/js/xgemius.js"></script>


<script type = "text/javascript">
<!--//--><![CDATA[//><!--
var _cm = {
 "baseUrl":('https:' == document.location.protocol ? 'https://' : 'http://') + 'ngacm.com/',

 "pv": true,
 "account": "CM.991213.tz_pl",
 "domain": ".allegro.pl"

};

(function() {
 var cm = document.createElement('script'); cm.type = 'text/javascript'; cm.async = true;
  cm.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'ngastatic.com/s4c/collect.js';
  var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(cm, s);
})();
//--><!]]>
</script>

  <script type="text/javascript" src="http://static.allegrostatic.pl/site_images/1/0/js/ado.js"></script>

<script src="http://static.allegrostatic.pl/js/libs/jquery-1.8.3_av.2013.37.4.min.js" type="text/javascript" charset="utf-8"></script>
<script type="text/javascript" charset="utf-8">var $j = jQuery.noConflict();</script>
<script src="http://static.allegrostatic.pl/js/libs/jquery-ui-1.9.2.custom_av.2013.37.4.min.js" type="text/javascript" charset="utf-8"></script>
<script src="http://static.allegrostatic.pl/js/libs/require-2.1.1_av.2013.37.4.min.js" type="text/javascript" charset="utf-8"></script>
<script src="http://static.allegrostatic.pl/js/libs/slimScroll_av.2013.37.4.min.js" type="text/javascript" charset="utf-8"></script>
<script src="http://static.allegrostatic.pl/js/scripts/jq_plugins_av.2013.37.4.min.js" type="text/javascript" charset="utf-8"></script>
<script src="http://static.allegrostatic.pl/js/scripts/mainjs-5_av.2013.37.4.min.js" type="text/javascript" charset="utf-8"></script>
<script src="http://static.allegrostatic.pl/js/scripts/vela-listing_av.2013.37.4.min.js" type="text/javascript" charset="utf-8"></script>
<script type="text/javascript">
//<![CDATA[

jQuery(function () {
require.config({"paths":{"async":"libs\/require-async","text":"libs\/require-text","tpl":"libs\/require-tpl","jquery":"libs\/jquery-1.8.3.min","jquery.ui":"libs\/jquery-ui-1.7.2.min","jquery.scrollTo":"libs\/jquery.scrollTo.min","jquery.multiSelect":"libs\/jquery.multi-select.min","jquery.simpleTree":"libs\/jquery.simpleTree.min","jquery.itemList":"libs\/jquery.itemList.min","underscore":"libs\/underscore.min","underscore.string":"libs\/underscore.string.min","backbone":"libs\/backbone.min","backbone.validation":"libs\/backbone.validation-amd.min","backbone.validation-msg-extension":"\/js\/scripts\/backbone.validation-msg-extension","backbone.validation-rules-extension":"\/js\/scripts\/backbone.validation-rules-extension","bootstrap":"\/js\/libs\/bootstrap.min","bootstrap-modal-extensions":"\/js\/scripts\/bootstrap-modal-extensions","accounting":"\/js\/libs\/accounting.min","marker-clusterer":"libs\/markerclusterer.min","collections":"scripts\/items-carousel\/collections","views":"scripts\/items-carousel\/views","main":"scripts\/items-carousel\/build\/items-carousel_av.2013.37.4.min"},"shim":{"jquery":{"exports":"jQuery"},"jquery.ui":{"deps":["jquery"]},"jquery.scrollTo":{"deps":["jquery"],"exports":"jQuery.fn.scrollTo"},"jquery.multiSelect":{"deps":["jquery"],"exports":"jQuery.fn.multiSelect"},"jquery.simpleTree":{"deps":["jquery"],"exports":"jQuery.fn.simpleTree"},"jquery.itemList":{"deps":["jquery"],"exports":"jQuery.fn.scrollTo"},"underscore":{"exports":"_"},"underscore.string":{"deps":["underscore"],"exports":"_s"},"backbone":{"deps":["jquery","underscore"],"exports":"Backbone"},"backbone.validation":{"deps":["backbone"]},"backbone.validation-msg-extension":{"deps":["backbone.validation"]},"backbone.validation-rules-extension":{"deps":["backbone.validation"]},"bootstrap-modal-extensions":{"deps":["bootstrap"]},"marker-clusterer":{"deps":["async!https:\/\/maps.google.com\/maps\/api\/js?sensor=false"],"exports":"MarkerClusterer"}},"baseUrl":"http:\/\/static.allegrostatic.pl\/js"});
define('jquery', function () { return jQuery; });
require.config({config:{text:{useXhr:function(){return true;}}}});
require(['main']);
});
jQuery(function () {
require.config({"paths":{"async":"libs\/require-async","text":"libs\/require-text","tpl":"libs\/require-tpl","jquery":"libs\/jquery-1.8.3.min","jquery.ui":"libs\/jquery-ui-1.7.2.min","jquery.scrollTo":"libs\/jquery.scrollTo.min","jquery.multiSelect":"libs\/jquery.multi-select.min","jquery.simpleTree":"libs\/jquery.simpleTree.min","jquery.itemList":"libs\/jquery.itemList.min","underscore":"libs\/underscore.min","underscore.string":"libs\/underscore.string.min","backbone":"libs\/backbone.min","backbone.validation":"libs\/backbone.validation-amd.min","backbone.validation-msg-extension":"\/js\/scripts\/backbone.validation-msg-extension","backbone.validation-rules-extension":"\/js\/scripts\/backbone.validation-rules-extension","bootstrap":"\/js\/libs\/bootstrap.min","bootstrap-modal-extensions":"\/js\/scripts\/bootstrap-modal-extensions","accounting":"\/js\/libs\/accounting.min","marker-clusterer":"libs\/markerclusterer.min","models":"scripts\/listing\/models","views":"scripts\/listing\/views","listing":"scripts\/listing\/build\/listing_av.2013.37.4.min"},"shim":{"jquery":{"exports":"jQuery"},"jquery.ui":{"deps":["jquery"]},"jquery.scrollTo":{"deps":["jquery"],"exports":"jQuery.fn.scrollTo"},"jquery.multiSelect":{"deps":["jquery"],"exports":"jQuery.fn.multiSelect"},"jquery.simpleTree":{"deps":["jquery"],"exports":"jQuery.fn.simpleTree"},"jquery.itemList":{"deps":["jquery"],"exports":"jQuery.fn.scrollTo"},"underscore":{"exports":"_"},"underscore.string":{"deps":["underscore"],"exports":"_s"},"backbone":{"deps":["jquery","underscore"],"exports":"Backbone"},"backbone.validation":{"deps":["backbone"]},"backbone.validation-msg-extension":{"deps":["backbone.validation"]},"backbone.validation-rules-extension":{"deps":["backbone.validation"]},"bootstrap-modal-extensions":{"deps":["bootstrap"]},"marker-clusterer":{"deps":["async!https:\/\/maps.google.com\/maps\/api\/js?sensor=false"],"exports":"MarkerClusterer"}},"baseUrl":"http:\/\/static.allegrostatic.pl\/js"});
define('jquery', function () { return jQuery; });
require.config({config:{text:{useXhr:function(){return true;}}}});
require(['listing']);
});
jQuery(function () {
require.config({"paths":{"async":"libs\/require-async","text":"libs\/require-text","tpl":"libs\/require-tpl","jquery":"libs\/jquery-1.8.3.min","jquery.ui":"libs\/jquery-ui-1.7.2.min","jquery.scrollTo":"libs\/jquery.scrollTo.min","jquery.multiSelect":"libs\/jquery.multi-select.min","jquery.simpleTree":"libs\/jquery.simpleTree.min","jquery.itemList":"libs\/jquery.itemList.min","underscore":"libs\/underscore.min","underscore.string":"libs\/underscore.string.min","backbone":"libs\/backbone.min","backbone.validation":"libs\/backbone.validation-amd.min","backbone.validation-msg-extension":"\/js\/scripts\/backbone.validation-msg-extension","backbone.validation-rules-extension":"\/js\/scripts\/backbone.validation-rules-extension","bootstrap":"\/js\/libs\/bootstrap.min","bootstrap-modal-extensions":"\/js\/scripts\/bootstrap-modal-extensions","accounting":"\/js\/libs\/accounting.min","marker-clusterer":"libs\/markerclusterer.min","vela-layout":"scripts\/vela-layout\/build\/vela-layout_av.2013.37.4.min"},"shim":{"jquery":{"exports":"jQuery"},"jquery.ui":{"deps":["jquery"]},"jquery.scrollTo":{"deps":["jquery"],"exports":"jQuery.fn.scrollTo"},"jquery.multiSelect":{"deps":["jquery"],"exports":"jQuery.fn.multiSelect"},"jquery.simpleTree":{"deps":["jquery"],"exports":"jQuery.fn.simpleTree"},"jquery.itemList":{"deps":["jquery"],"exports":"jQuery.fn.scrollTo"},"underscore":{"exports":"_"},"underscore.string":{"deps":["underscore"],"exports":"_s"},"backbone":{"deps":["jquery","underscore"],"exports":"Backbone"},"backbone.validation":{"deps":["backbone"]},"backbone.validation-msg-extension":{"deps":["backbone.validation"]},"backbone.validation-rules-extension":{"deps":["backbone.validation"]},"bootstrap-modal-extensions":{"deps":["bootstrap"]},"marker-clusterer":{"deps":["async!https:\/\/maps.google.com\/maps\/api\/js?sensor=false"],"exports":"MarkerClusterer"}},"baseUrl":"http:\/\/static.allegrostatic.pl\/js"});
define('jquery', function () { return jQuery; });
require.config({config:{text:{useXhr:function(){return true;}}}});
require(['vela-layout']);
});
$j("a[rel=external]").attr("target","_blank");

if(typeof ado!=="object"){ado={};ado.config=ado.preview=ado.placement=ado.master=ado.slave=function(){};}
ado.config({mode: "new", xml: false, characterEncoding: true});

/* (c)AdOcean 2003-2011 */




 var _adoCalls = _adoCalls || [];
 var _cmParams = _cmParams || [];

 var allAdocean = {
 'intervalCount' : 0,
 'interval' : null,
 'showAds' : function() {
 allAdocean.interval = setInterval(
 function() {
 $j('[data-adocean-id]').each(
 function() {
 if ($j(this).find('[data-ad]').contents().length) {
 var adType = $j(this).attr('data-adocean-id');
 $j('[data-showcase-id="'+adType+'"]').hide();
 $j(this).show();

 if (adType === 'c_top_300_250') {
 $j('#showCatAdvertOne').css('padding-bottom', '10px');
 }
 if (adType === 'c_bottom_300_250') {
 $j('#showCatAdvertTwo').css('padding-bottom', '10px');
 }
 if (adType === 'l_header_750_100' || adType === 'l_header_970_100' || adType === 'c_header_970_100' || adType === 'c_header_750_100' || adType === 'm_header_750_100' || adType === 'm_header_970_100') {
  var adoceanHeader = $j('#adoceanHeader');
 adoceanHeader.remove();
 $j('#wrapper').before(adoceanHeader);
 if ($j.browser.webkit) {
 $j('body').css('zoom', '100.00001%');
 }

 }
 if (adType === 'l_left_top_160_600' || adType === 'l_left_bottom_160_600') {
 $j('#isAdvert').show();
 }

 clearInterval(allAdocean.interval);
 }
 }
 );
 allAdocean.intervalCount++;
 if (allAdocean.intervalCount > 5) {
 clearInterval(allAdocean.interval);
 }
 },
 700
 )
 }
 }

 _cmParams.push({ path: "niemaczegos"});




  ado.preview
({enabled: true,
emiter: "gg.adocean.pl"});


_adoCalls.push
({type: "master", params: {
id: "MTc80m713Q7UstlQBQWhvXr8XTOT58enUIv4_1KKHiT.N7"
, server: "gg.adocean.pl", keys: ["","niemaczegos"]}});

  _adoCalls.push(
{
type: "slave",
slaveId: "adoceangglgmsmtqoxj",
params: {
myMaster: "MTc80m713Q7UstlQBQWhvXr8XTOT58enUIv4_1KKHiT.N7"
}});
  _adoCalls.push(
{
type: "slave",
slaveId: "adoceanggwahqcklrae",
params: {
myMaster: "MTc80m713Q7UstlQBQWhvXr8XTOT58enUIv4_1KKHiT.N7"
}});
  _adoCalls.push(
{
type: "slave",
slaveId: "adoceanggtboggxegud",
params: {
myMaster: "MTc80m713Q7UstlQBQWhvXr8XTOT58enUIv4_1KKHiT.N7"
}});
    _adoCalls.push({type: "afterCallback", callback: allAdocean.showAds});

 (function() {
 var cm = document.createElement('script'); cm.type = 'text/javascript'; cm.async = true;
 cm.src = 'http://adct.gg.pl/ct.js';
 var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(cm, s);
 })();



//]]>
</script> </body>
</html>'''


class MyTest(unittest.TestCase):

    @mock.patch('allegro.lib.mechanize.Browser')
    def test(self, Browser):
        ALLEGRO_KEY = 'A_KEY'
        browser = Browser()
        browser.response().read.return_value = EXAMPLE_HTML
        self.assertEquals(
            downolad_data(ALLEGRO_KEY),
            (
                'http://allegro.pl/laptop-samsung-i5-3210m-gt650-8gb-1000gb-windows-8-i3332485440.html',
                2739.00
            )
        )

    @mock.patch('allegro.lib.mechanize.Browser')
    def test_error(self, Browser):
        browser = Browser()
        browser.response().read.return_value = EXAMPLE_ERROR
        self.assertRaises(
            AllegroError,
            downolad_data,
            'A_KEY'
        )


if __name__ == "__main__":
    unittest.main()
