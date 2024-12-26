
// table ใบแจ้งซ่อม
$(document).ready(function() {
    $('#table-pending').DataTable({
        paging: true,     
        searching: true,   
        ordering: true,     
        info: true,          
    });

    $('#table-process').DataTable({
        paging: true,
        searching: true,
        ordering: true,
        info: true
    })
    $('#table-completed').DataTable({
        paging: true,
        searching: true,
        ordering: true,
        info: true,
        "scrollX": true,
        "responsive": true 
    });

    $('#table-canceled').DataTable({
        paging: true,
        searching: true,
        ordering: true,
        info: true
    })

    $('#table-claim').DataTable({
        paging: true,
        searching: true,
        ordering: true,
        info: true
    })

    $('#table-computer').DataTable({

    })
    
    $('#table-software').DataTable({

    })

    $('#table-monitor').DataTable({

    })
    
    $('#table-mouse').DataTable({

    })

    $('#table-keyboard').DataTable({

    })

    $('#table-printer').DataTable({

    })

    $('#table-scanner').DataTable({

    })

    $('#table-server').DataTable({

    })

    $('#table-ups').DataTable({

    })

    $('#table-network').DataTable({

    })

    $('#table-cctv').DataTable({

    })

    $('#table-tablet').DataTable({

    })

    $('#table-other').DataTable({
        
    })
});

