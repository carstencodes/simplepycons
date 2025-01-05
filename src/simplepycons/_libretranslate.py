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


class LibretranslateIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "libretranslate"

    @property
    def original_file_name(self) -> "str":
        return "libretranslate.svg"

    @property
    def title(self) -> "str":
        return "LibreTranslate"

    @property
    def primary_color(self) -> "str":
        return "#1565C0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>LibreTranslate</title>
     <path d="M13.7835 0q-1.7162 4.666-8.892 7.991l1.3623
 1.523q5.3951-2.6385 7.8192-5.996 2.4777 3.1857 8.1948 6.1247L23.544
 8.066q-6.103-2.9283-8.4198-6.2425.118-.1824.4827-1.255ZM9.5467
 7.991q-.3218 3.5075-1.4481 5.8028-1.1155 2.2953-3.6683 4.5692l1.4265
 1.2763q2.8426-2.6064 4.1941-5.556 1.1799 1.0297 2.4133
 2.6494l1.4588-1.3086q-1.1477-1.4587-3.2286-3.25.547-2.0271.7614-3.9793zm7.1007
 0q-.1716 4.151-1.4158 6.3927-1.2444 2.2417-3.7328 3.8934l1.4051
 1.298q3.5718-2.6065 4.7088-5.8242 1.7268 3.4644 4.8696
 5.867l1.4051-1.3408q-1.7806-1.3192-3.0141-2.7887-1.2227-1.4801-1.8662-3.0461-.6328-1.5767-.6328-2.1452l.075-.751q.0859-.8366.0859-1.3942zM.1126
 8.8018V24h9.4443v-1.7095H2.0515V8.8018Z" />
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
