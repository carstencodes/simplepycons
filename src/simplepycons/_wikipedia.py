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


class WikipediaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wikipedia"

    @property
    def original_file_name(self) -> "str":
        return "wikipedia.svg"

    @property
    def title(self) -> "str":
        return "Wikipedia"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Wikipedia</title>
     <path d="M12.09 13.119c-.936 1.932-2.217 4.548-2.853 5.728-.616
 1.074-1.127.931-1.532.029-1.406-3.321-4.293-9.144-5.651-12.409-.251-.601-.441-.987-.619-1.139-.181-.15-.554-.24-1.122-.271C.103
 5.033 0 4.982 0 4.898v-.455l.052-.045c.924-.005 5.401 0 5.401
 0l.051.045v.434c0
 .119-.075.176-.225.176l-.564.031c-.485.029-.727.164-.727.436 0
 .135.053.33.166.601 1.082 2.646 4.818 10.521 4.818 10.521l.136.046
 2.411-4.81-.482-1.067-1.658-3.264s-.318-.654-.428-.872c-.728-1.443-.712-1.518-1.447-1.617-.207-.023-.313-.05-.313-.149v-.468l.06-.045h4.292l.113.037v.451c0
 .105-.076.15-.227.15l-.308.047c-.792.061-.661.381-.136 1.422l1.582
 3.252
 1.758-3.504c.293-.64.233-.801.111-.947-.07-.084-.305-.22-.812-.24l-.201-.021c-.052
 0-.098-.015-.145-.051-.045-.031-.067-.076-.067-.129v-.427l.061-.045c1.247-.008
 4.043 0 4.043 0l.059.045v.436c0
 .121-.059.178-.193.178-.646.03-.782.095-1.023.439-.12.186-.375.589-.646
 1.039l-2.301 4.273-.065.135 2.792 5.712.17.048
 4.396-10.438c.154-.422.129-.722-.064-.895-.197-.172-.346-.273-.857-.295l-.42-.016c-.061
 0-.105-.014-.152-.045-.043-.029-.072-.075-.072-.119v-.436l.059-.045h4.961l.041.045v.437c0
 .119-.074.18-.209.18-.648.03-1.127.18-1.443.421-.314.255-.557.616-.736
 1.067 0 0-4.043 9.258-5.426 12.339-.525
 1.007-1.053.917-1.503-.031-.571-1.171-1.773-3.786-2.646-5.71l.053-.036z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Wikip'''

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
