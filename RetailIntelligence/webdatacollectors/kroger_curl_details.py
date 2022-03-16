headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'X-Sec-Clge-Req-Type': 'ajax',
    'x-laf-object': '[{"fallbackDestination":"02500624","createdDate":1647442935212,"destination":{"address":{"postalCode":"72801"},"location":{"lat":35.27838134765625,"lng":-93.14070892333984}},"id":"c18568fc-8e74-4e23-a318-890943ed6c6f","fallbackFulfillment":"491DC001","modalityType":"SHIP","source":"SHIP_AUTOGEN","fulfillment":["491DC001","309DC309","310DC310","DSV00001","MKTPLACE"],"isTrustedSource":false},{"fallbackFulfillment":"02500624","createdDate":1647442935214,"destination":{"locationId":"02500624"},"id":"34a6c904-d101-4485-aaa9-dc771fd07911","isCrossBanner":false,"modalityType":"PICKUP","source":"FALLBACK_ACTIVE_MODALITY_COOKIE","fulfillment":["02500624"],"isTrustedSource":false}]',
    'x-kroger-feature-USE-V2-COMPOSITE': 'true',
    'X-Kroger-Channel': 'WEB',
    'x-call-origin': '{"component":"browse products","page":"browse products"}',
    'x-modality': '{"type":"PICKUP","locationId":"02500624"}',
    'x-ab-test': '[{"testVersion":"A","testID":"413ee4","testOrigin":"TL"}]',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Referer': 'https://www.kroger.com/pl/fresh-fruit/06111',
    'Connection': 'keep-alive',
    'TE': 'trailers',
}

params_page1 = (
    ('filter.gtin13s',
     ['0000000004011', '0003338320027', '0001111069102', '0000000004225', '0001111069106', '0001111004654',
      '0001111018225', '0000000004023', '0000000004046', '0000000094011', '0001111018209', '0000000004053',
      '0000000004022', '0000000004048', '0003338321000', '0000000003283', '0003338322101', '0003338322241',
      '0003338324000', '0000000004430', '0000000004045', '0003338320030', '0000000004032', '0000000004134',
      '0000000003107', '0003338320038', '0000000004050', '0000000004131', '0000000004959']),
    ('filter.verified', 'true'),
    ('projections', 'items.full,variantGroupings.compact'),
)

params_page2 = (
    ('filter.gtin13s',
     ['0000000004012', '0000000003421', '0007224013381', '0000000004056', '0001111003931', '0001111090032',
      '0001111001680', '0001111001615', '0000000004409', '0000000004017', '0001111018221', '0001111091188',
      '0001111018189', '0001111091825', '0001111060197', '0000000004281', '0005916550200', '0079144700004',
      '0001111001616', '0000000004040', '0000000004030', '0000000004130', '0000000004416', '0000000094225',
      '0001111091189', '0001111069101', '0001111018180', '0000000004958']),
    ('filter.verified', 'true'),
    ('projections', 'items.full,variantGroupings.compact'),
)

params_page3 = (
    ('filter.gtin13s',
     ['0003338324001', '0071575610022', '0000000093283', '0775487900029', '0775014200038', '0000000094053',
      '0000000004413', '0000000094023', '0000000003616', '0001111018188', '0000000094022', '0000000003507',
      '0001111091829', '0000000004235', '0000000004034', '0001111018233', '0003022308160', '0005410740200',
      '0000000003618', '0001111018999']),
    ('filter.verified', 'true'),
    ('projections', 'items.full,variantGroupings.compact'),
)

params_page4 = (
    ('filter.gtin13s',
     ['0000000094048', '0001111069103', '0000000004051', '0000000004417', '0000000004031', '0001111018199',
      '0000000094131', '0000000003438', '0000000003632', '0001111014902', '0000000004016', '0003022308162',
      '0000000003488', '0000000003094', '0000000004636', '0082890400087', '0003022308164', '0085085900262',
      '0775430500253', '0000000003040', '0000000004312', '0003022308154', '0003022308230']),
    ('filter.verified', 'true'),
    ('projections', 'items.full,variantGroupings.compact'),
)

params_page5 = (
    ('filter.gtin13s', ['0001111004404', '0007224054678', '0003022308312', '0000000094959', '0000000094281', '0060504944769', '0000000003294', '0001111018195', '0000000003486', '0000000003601', '0003022308155', '0003022308159', '0003022308231', '0000000094430', '0000000003293', '0003022308229', '0003022308172', '0000000004961', '0003022310438', '0000000003111', '0085142600213']),
    ('filter.verified', 'true'),
    ('projections', 'items.full,variantGroupings.compact'),
)
