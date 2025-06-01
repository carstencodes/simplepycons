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


class SonarqubeForIdeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sonarqubeforide"

    @property
    def original_file_name(self) -> "str":
        return "sonarqubeforide.svg"

    @property
    def title(self) -> "str":
        return "SonarQube for IDE"

    @property
    def primary_color(self) -> "str":
        return "#126ED3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SonarQube for IDE</title>
     <path d="M12.4219.002a12.0453 12.0453 0 0
 0-.5274.002c-2.8105.0773-5.6 1.1307-7.7968
 3.1522-.328.3024-.3306.8227-.0118
 1.1329l.002.002.0041.0039c.2993.2729.7594.2765 1.0564 0 1.9339-1.774
 4.4298-2.6978 6.8536-2.7442 2.4237-.0464 4.868.739 6.8535
 2.3789.3145.2578.775.2366
 1.0586-.0625.3094-.325.2771-.846-.0684-1.1348C17.6894.9533
 15.0583.045 12.4219.002ZM6.996 9.668c-1.2996 0-1.908 1.1345-2.3516
 1.9648-.3764.7117-.6362 1.1465-.9765 1.1465-.3404
 0-.593-.4348-.9746-1.1465-.2785-.5208-.618-1.159-1.1543-1.5664-.49-.3661-1.1914-.0063-1.1914.6074v.125c0
 .2218.1188.407.289.541.2166.1702.4174.531.6856 1.0313.4435.8303 1.052
 1.9648 2.3515 1.9648 1.2996 0 1.908-1.1345
 2.3516-1.9648.3816-.7117.635-1.1445.9805-1.1445.3455 0
 .5969.4328.9785 1.1445.4435.8303 1.0571 1.9648 2.3515 1.9648 1.2944 0
 1.9042-1.1345 2.3477-1.9648.3765-.7117.629-1.1445.9746-1.1445.3455 0
 .5989.4328.9805 1.1445.4435.8303 1.052 1.9648 2.3515 1.9648 1.2996 0
 1.9081-1.1345 2.3516-1.9648.3816-.7117.6382-1.1445.9785-1.1445.3404 0
 .5989.4328.9805 1.1445.2785.5208.6238 1.161 1.1601 1.5684.49.3661
 1.1914.0043
 1.1914-.6094h-.0098v-.123c0-.2167-.1188-.409-.289-.543-.2166-.1702-.4233-.531-.6914-1.0313-.4435-.8303-1.052-1.9648-2.3516-1.9648-1.2995
 0-1.908 1.1345-2.3516 1.9648-.3816.7117-.6349 1.1465-.9804
 1.1465-.3455
 0-.597-.4348-.9785-1.1465-.4435-.8303-1.0572-1.9648-2.3516-1.9648s-1.9042
 1.1345-2.3477 1.9648c-.3764.7117-.629 1.1465-.9746 1.1465-.3455
 0-.5969-.4348-.9785-1.1465-.4434-.8303-1.052-1.9648-2.3515-1.9648Zm12.2832
 10.0254c-1.8514 1.707-4.2337 2.677-6.7813
 2.7441-2.5475.0722-4.9776-.768-6.9218-2.377-.3198-.2578-.7789-.2385-1.0625.0606-.3094.3249-.283.8511.0625
 1.1348C6.7266 23.035 9.3977 24 12.2032
 24l.0116-.0098h.3301c2.924-.0774 5.662-1.1914
 7.7969-3.1563.3249-.3094.3249-.8312
 0-1.1406-.299-.2784-.7585-.2782-1.0625 0z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

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
