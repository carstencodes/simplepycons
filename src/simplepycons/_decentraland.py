#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class DecentralandIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "decentraland"

    @property
    def original_file_name(self) -> "str":
        return "decentraland.svg"

    @property
    def title(self) -> "str":
        return "Decentraland"

    @property
    def primary_color(self) -> "str":
        return "#FF2D55"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Decentraland</title>
     <path d="M16.9246
 18.9776h3.1342l-3.1342-3.7778Zm-8.507-9.4221v6.6221h5.5072ZM12.0442
 0C5.4177 0 0 5.3333 0 11.9555c0 1.4666.2687 2.8888.7612
 4.1777l4.6565-5.5555L8.104 7.3333l6.537 7.8221 1.8805-2.2666 4.9252
 5.8666h.403c1.388-1.9555 2.1491-4.311 2.1491-6.8444C24.0885 5.3333
 18.6708 0 12.0442 0ZM8.0593 6.2666c-.9402
 0-1.6566-.7555-1.6566-1.6444 0-.8889.7612-1.6444 1.6566-1.6444.9403 0
 1.6567.7555 1.6567 1.6444 0 .8889-.7164 1.6444-1.6567 1.6444zm8.731
 5.3777c-1.8358 0-3.3133-1.4666-3.3133-3.2888 0-1.8222 1.4775-3.2889
 3.3133-3.2889 1.8357 0 3.3133 1.4667 3.3133 3.2889.0447 1.8222-1.4776
 3.2888-3.3133 3.2888zm-3.985 5.7334H1.1642c.2686.5333.582 1.0222.8955
 1.511h9.4473ZM4.4776 21.422h14.9993c.4925-.4 1.0298-.8889
 1.3432-1.2444H3.1343c.4477.4444.8954.8889 1.3432 1.2444zm7.5668
 2.5777c1.97 0 3.8506-.4444 5.5072-1.2889H6.5371C8.1937 23.5554
 10.0295 24 12.0443 24z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/decentraland/catalyst/issu'''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
