import time
import subprocess

data = [
    ['990108638184702204', 'URN:NBN:no-25522'],
    ['990706789014702204', 'URN:NBN:no-25523'],
    ['990717961854702204', 'URN:NBN:no-25524'],
    ['999104689154702204', 'URN:NBN:no-25525'],
    ['999600196344702204', 'URN:NBN:no-25526'],
    ['990827159474702204', 'URN:NBN:no-25527'],
    ['990717968354702204', 'URN:NBN:no-25528'],
    ['990717958984702204', 'URN:NBN:no-25580'],
    ['990717963124702204', 'URN:NBN:no-25581'],
    ['999307133544702204', 'URN:NBN:no-25582'],
    ['990717960294702204', 'URN:NBN:no-25583'],
    ['990717958634702204', 'URN:NBN:no-25584'],
    ['999814378424702204', 'URN:NBN:no-25585'],
    ['999612263404702204', 'URN:NBN:no-25586'],
    ['999612268114702204', 'URN:NBN:no-25587'],
    ['990717836284702204', 'URN:NBN:no-25588'],
    ['990717964364702204', 'URN:NBN:no-25589'],
    ['990717964874702204', 'URN:NBN:no-25590'],
    ['990717958044702204', 'URN:NBN:no-25591'],
    ['990717957744702204', 'URN:NBN:no-25593'],
    ['990717830324702204', 'URN:NBN:no-25594'],
    ['990717969754702204', 'URN:NBN:no-25595'],
    ['990111032134702204', 'URN:NBN:no-25596'],
    ['990111032304702204', 'URN:NBN:no-25597'],
    ['990111032484702204', 'URN:NBN:no-25598'],
    ['990111032564702204', 'URN:NBN:no-25599'],
    ['990717960704702204', 'URN:NBN:no-25600'],
    ['990827652864702204', 'URN:NBN:no-25601'],
    ['999710473674702204', 'URN:NBN:no-25602'],
    ['990717967114702204', 'URN:NBN:no-25603'],
    ['990717966064702204', 'URN:NBN:no-25604'],
    ['990717834664702204', 'URN:NBN:no-25605'],
    ['990604423604702204', 'URN:NBN:no-26117'],
    ['990217044814702204', 'URN:NBN:no-26118'],
    ['999324491584702204', 'URN:NBN:no-26119'],
    ['999327847804702204', 'URN:NBN:no-26120'],
    ['999803642804702204', 'URN:NBN:no-27552'],
    ['999718042734702204', 'URN:NBN:no-27553'],
    ['999706272204702204', 'URN:NBN:no-27554'],
    ['990700983284702204', 'URN:NBN:no-27555'],
    ['990604489624702204', 'URN:NBN:no-27556'],
    ['990604467224702204', 'URN:NBN:no-27557'],
    ['990706950404702204', 'URN:NBN:no-27558'],
    ['998903320884702204', 'URN:NBN:no-27559'],
    ['999209695694702204', 'URN:NBN:no-27561'],
    ['999008625484702204', 'URN:NBN:no-27562'],
    ['999001421464702204', 'URN:NBN:no-27563'],
    ['999420705774702204', 'URN:NBN:no-27564'],
    ['999826005694702204', 'URN:NBN:no-27567'],
    ['999810003124702204', 'URN:NBN:no-27568'],
    ['998011820774702204', 'URN:NBN:no-27569'],
    ['999803404034702204', 'URN:NBN:no-27570'],
    ['999714714104702204', 'URN:NBN:no-27571'],
    ['990925953084702204', 'URN:NBN:no-27572'],
    ['999218373054702204', 'URN:NBN:no-27573'],
    ['990706890834702204', 'URN:NBN:no-27574'],
    ['990412511134702204', 'URN:NBN:no-27575'],
    ['990706702934702204', 'URN:NBN:no-27576'],
    ['990706700304702204', 'URN:NBN:no-27577'],
    ['999204912944702204', 'URN:NBN:no-27695'],
    ['999002599904702204', 'URN:NBN:no-29080'],
    ['990318769434702204', 'URN:NBN:no-29469'],
    ['999205918414702204', 'URN:NBN:no-29470'],
    ['999427669114702204', 'URN:NBN:no-29471'],
    ['999523991304702204', 'URN:NBN:no-29472'],
    ['999320417104702204', 'URN:NBN:no-29473'],
    ['999718076634702204', 'URN:NBN:no-29474'],
    ['999900043684702204', 'URN:NBN:no-29475'],
    ['999901294204702204', 'URN:NBN:no-29476'],
    ['998903479564702204', 'URN:NBN:no-29477'],
    ['990108617504702204', 'URN:NBN:no-29479'],
    ['990122794714702204', 'URN:NBN:no-29480'],
    ['990117553694702204', 'URN:NBN:no-29481'],
    ['999517115124702204', 'URN:NBN:no-29483'],
    ['998820044334702204', 'URN:NBN:no-29484'],
    ['990204594834702204', 'URN:NBN:no-29485'],
    ['999209695504702204', 'URN:NBN:no-29486'],
    ['999321629674702204', 'URN:NBN:no-29529'],
    ['999421783434702204', 'URN:NBN:no-29530'],
    ['990205932874702204', 'URN:NBN:no-29531'],
    ['990934422624702204', 'URN:NBN:no-29532'],
    ['999401323894702204', 'URN:NBN:no-29534'],
    ['990937006014702204', 'URN:NBN:no-29535'],
    ['990506452694702204', 'URN:NBN:no-29536'],
    ['999726395004702204', 'URN:NBN:no-29537'],
    ['990933929234702204', 'URN:NBN:no-29538'],
    ['999800407604702204', 'URN:NBN:no-29539'],
    ['990202168664702204', 'URN:NBN:no-29540'],
    ['990604761844702204', 'URN:NBN:no-29542'],
    ['990604762734702204', 'URN:NBN:no-29543'],
    ['999429579544702204', 'URN:NBN:no-29544'],
    ['990938422524702204', 'URN:NBN:no-29545'],
    ['990417383224702204', 'URN:NBN:no-29546'],
    ['990417976394702204', 'URN:NBN:no-29547'],
    ['990418298594702204', 'URN:NBN:no-29548'],
    ['999012737324702204', 'URN:NBN:no-29549'],
    ['999724817454702204', 'URN:NBN:no-29550'],
    ['999813386904702204', 'URN:NBN:no-29783'],
    ['990108741434702204', 'URN:NBN:no-29784'],
    ['990200699444702204', 'URN:NBN:no-29785'],
    ['990601318964702204', 'URN:NBN:no-29786'],
    ['990102108654702204', 'URN:NBN:no-29787'],
    ['990208261414702204', 'URN:NBN:no-29788'],
    ['990123020744702204', 'URN:NBN:no-29789'],
    ['990220992204702204', 'URN:NBN:no-29790'],
    ['999724469744702204', 'URN:NBN:no-29791'],
    ['990601228034702204', 'URN:NBN:no-29792'],
    ['990601051354702204', 'URN:NBN:no-29793'],
    ['999600401964702204', 'URN:NBN:no-29794'],
    ['999320499074702204', 'URN:NBN:no-29795'],
    ['999615271294702204', 'URN:NBN:no-29796'],
    ['999600207724702204', 'URN:NBN:no-29797'],
    ['999323209104702204', 'URN:NBN:no-29798'],
    ['990204513004702204', 'URN:NBN:no-29799'],
    ['999600195454702204', 'URN:NBN:no-29800'],
    ['990224652944702204', 'URN:NBN:no-29801'],
    ['999613458964702204', 'URN:NBN:no-29802'],
    ['999615261904702204', 'URN:NBN:no-29803'],
    ['999615271964702204', 'URN:NBN:no-29804'],
    ['999615263784702204', 'URN:NBN:no-29805'],
    ['999601829854702204', 'URN:NBN:no-29806'],
    ['999615273154702204', 'URN:NBN:no-29807'],
    ['999405700684702204', 'URN:NBN:no-29808'],
    ['990501538114702204', 'URN:NBN:no-29809'],
    ['999519228074702204', 'URN:NBN:no-29810'],
    ['999417724034702204', 'URN:NBN:no-29811'],
    ['999612195994702204', 'URN:NBN:no-29812'],
    ['991144059564702204', 'URN:NBN:no-29860'],
    ['999008837824702204', 'URN:NBN:no-30030'],
    ['998550046654702204', 'URN:NBN:no-30031'],
    ['990226196584702204', 'URN:NBN:no-30195'],
    ['999601093154702204', 'URN:NBN:no-30876'],
    ['999008587104702204', 'URN:NBN:no-30877'],
    ['990412326154702204', 'URN:NBN:no-30878'],
    ['999600196004702204', 'URN:NBN:no-30879'],
    ['999600195964702204', 'URN:NBN:no-30880'],
    ['999419173474702204', 'URN:NBN:no-30881'],
    ['990511883924702204', 'URN:NBN:no-30882'],
    ['990511772424702204', 'URN:NBN:no-30883'],
    ['999610943544702204', 'URN:NBN:no-32518'],
    ['999525599274702204', 'URN:NBN:no-32519'],
    ['999526171294702204', 'URN:NBN:no-32521'],
    ['990610795374702204', 'URN:NBN:no-33069'],
    ['999112068844702204', 'URN:NBN:no-33070'],
    ['999108596124702204', 'URN:NBN:no-33071'],
    ['999706850174702204', 'URN:NBN:no-33072'],
    ['999215239394702204', 'URN:NBN:no-33073'],
    ['999517486614702204', 'URN:NBN:no-33074'],
    ['999220417924702204', 'URN:NBN:no-33075'],
    ['999220417174702204', 'URN:NBN:no-33076'],
    ['999220418654702204', 'URN:NBN:no-33077'],
    ['999220418304702204', 'URN:NBN:no-33078'],
    ['998030193514702204', 'URN:NBN:no-33079'],
    ['998870431784702204', 'URN:NBN:no-33080'],
    ['998870356474702204', 'URN:NBN:no-33081'],
    ['990931767164702204', 'URN:NBN:no-33082'],
    ['999323720664702204', 'URN:NBN:no-33083'],
    ['990112794194702204', 'URN:NBN:no-33084'],
    ['999723951484702204', 'URN:NBN:no-33085'],
    ['998421021594702204', 'URN:NBN:no-33086'],
    ['999324648904702204', 'URN:NBN:no-33087'],
    ['999425559294702204', 'URN:NBN:no-33088'],
    ['999425559704702204', 'URN:NBN:no-33089'],
    ['991214009804702204', 'URN:NBN:no-33090'],
    ['991227593384702204', 'URN:NBN:no-33091'],
    ['991227595594702204', 'URN:NBN:no-33187'],
    ['991227595914702204', 'URN:NBN:no-33476'],
    ['999505092644702204', 'URN:NBN:no-34018'],
]

for job in data:
    command = ['saturn', 'add', '--update_urns', '--urn', job[1], job[0]]
    print(' '.join(command))
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, error = proc.communicate()
    print(output.decode('utf-8'))
    time.sleep(3)
