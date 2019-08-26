---
title: "Anmeldung"
bg: 'red'
color: black
fa-icon: check-circle
---

## Registrierung

Die Registrierung ist ab dem 2. September 2019 möglich.

<!-- You can customize this button any way you like -->
<button id="eventbrite-widget-modal-trigger-69705638441" type="button">Ticket kaufen</button>

<!-- Noscript content for added SEO -->
<noscript><a href="https://www.eventbrite.de/e/swacamp-munich-2019-tickets-69705638441" rel="noopener noreferrer" target="_blank">
Ticket über Eventbrite kaufen</a></noscript>


<script src="https://www.eventbrite.de/static/widgets/eb_widgets.js"></script>

<script type="text/javascript">
    var exampleCallback = function() {
        console.log('Order complete!');
    };

    window.EBWidgets.createWidget({
        widgetType: 'checkout',
        eventId: '69705638441',
        modal: true,
        modalTriggerElementId: 'eventbrite-widget-modal-trigger-69705638441',
        onOrderComplete: exampleCallback
    });
</script>

