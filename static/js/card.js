const isInBetween = (value, minimum, maximum) => {
    return minimum < value && value < maximum;
}

const getCardGroups = () => {
    const cardGroupElements = document.getElementsByClassName('card-group');
    const cardGroups = {};
    for (let element of cardGroupElements) {
        const cardGroupTitle = element.querySelector('.card-group-title h3');
        const cardGroupName = cardGroupTitle.textContent;

        const cardGroupTop = element.offsetTop;
        const cardGroupBottom = cardGroupTop + element.offsetHeight;
        cardGroups[cardGroupName] = {
            'element': cardGroupTitle,
            'interval': [cardGroupTop, cardGroupBottom],
        };
    }
    return cardGroups;
}


const trackCurrentCardGroup = () => {
    const currentScrollY = window.scrollY;
    const cardGroups = getCardGroups();
    for (let cardGroupName in cardGroups) {
        let cardGroupObject = cardGroups[cardGroupName];
        let element = cardGroupObject['element'];
        let interval = cardGroupObject['interval'];
        const delta = window.scrollY - interval[0];
        const elementHeight = parseFloat(window.getComputedStyle(element).getPropertyValue('height'));
        if (isInBetween(window.scrollY, interval[0], interval[1]) &&
            isInBetween(interval[0] + delta + 2 * elementHeight, interval[0], interval[1])) {    
            element.style.paddingTop = delta + 'px';
        } else {
            element.style.paddingTop = '0px';
        }
    }
}

const addOnScrollListener = () => {
    const body = document.getElementsByTagName('body')[0];
    const screenMdWidth = 768;
    body.onscroll = (e) => {
        if (window.innerWidth > screenMdWidth) {
            trackCurrentCardGroup();
        }
    }
}

const init = () => {
    addOnScrollListener();
}