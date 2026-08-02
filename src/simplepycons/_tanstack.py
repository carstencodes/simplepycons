#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class TanstackIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tanstack"

    @property
    def original_file_name(self) -> "str":
        return "tanstack.svg"

    @property
    def title(self) -> "str":
        return "TanStack"

    @property
    def primary_color(self) -> "str":
        return "#ECE8D1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>TanStack</title>
     <path d="M12 0c6.627 0 9.166 4.102 9.166 12S18.626 24 12
 24s-9.166-4.096-9.166-12c0-7.898 2.54-12 9.166-12m3.031 17.485c-.861
 0-1.33.234-1.708.423-.327.164-.582.292-1.148.292-.567
 0-.822-.128-1.148-.292-.378-.189-.848-.423-1.71-.423-.86
 0-1.33.234-1.708.423-.327.164-.581.292-1.148.292v1.251c.862 0
 1.331-.234 1.709-.423.326-.163.581-.292 1.148-.292s.821.129
 1.148.292c.378.189.847.423 1.709.423.861 0 1.33-.234
 1.709-.423.326-.163.58-.292 1.147-.292s.822.129
 1.148.292c.378.189.848.423 1.71.423v-1.25c-.565
 0-.822-.13-1.149-.293-.377-.189-.847-.423-1.709-.423m.41-12.536c.65-.586
 0-1.648-.813-1.328-.45.18-.873.438-1.251.779a4.2 4.2 0 0 0-1.202 1.94
 4.2 4.2 0 0 0-1.203-1.94 4.3 4.3 0 0
 0-1.25-.779c-.814-.32-1.463.742-.814 1.328l2.385 2.153a4.86 4.86 0 0
 0-2.731-.839c-.552 0-1.082.09-1.58.26-.836.284-.604 1.532.275
 1.532h3.326a4.2 4.2 0 0 0-2.012.988 4 4 0 0 0-.9 1.165c-.403.776.588
 1.529 1.237.948l2.686-2.42-.2 6.656c0 .08-.047.158-.107.223a5 5 0 0
 1-.257-.123c-.378-.189-.848-.423-1.71-.423-.861
 0-1.33.234-1.708.423-.327.164-.581.292-1.148.292v1.251c.861 0
 1.33-.234 1.709-.423.326-.164.58-.292 1.148-.292.566 0 .821.128
 1.148.292.377.189.847.423 1.708.423.862 0 1.332-.234
 1.71-.423.326-.164.58-.292 1.147-.292s.822.128
 1.148.292c.378.189.848.423 1.71.423v-1.25c-.565
 0-.822-.13-1.149-.293v-.005c-.378-.19-.847-.424-1.709-.424-.861
 0-1.33.235-1.709.424-.097.045-.189.094-.283.131a.34.34 0 0
 1-.12-.232l-.2-6.69 2.722 2.457c.65.587 1.64-.166 1.236-.948a4.11
 4.11 0 0 0-2.911-2.153h3.326c.882 0 1.108-1.245.275-1.531a4.88 4.88 0
 0 0-4.311.578l2.385-2.152z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://tanstack.com/images/brand/tanstack-em'''

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
