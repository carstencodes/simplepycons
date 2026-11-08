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


class OceanbaseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "oceanbase"

    @property
    def original_file_name(self) -> "str":
        return "oceanbase.svg"

    @property
    def title(self) -> "str":
        return "OceanBase"

    @property
    def primary_color(self) -> "str":
        return "#0181FD"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>OceanBase</title>
     <path d="M13.074 19.846a23 23 0 0 1 2.11-.768l.547-.157A21.8 21.8
 0 0 1 24 18.244v-2.826a24.6 24.6 0 0
 0-9.142.821l-.547.156c-.234.078-.482.156-.716.234-.469.156-.938.339-1.393.521l.872
 2.683ZM23.987 6.264v8.451a25 25 0 0
 0-9.467.899c-.391.117-.768.234-1.159.364-.469.156-.938.313-1.394.443A33.6
 33.6 0 0 1 .013 17.723V9.272c3.073.3 6.238.026
 9.35-.86.43-.117.846-.26 1.276-.403s.859-.286 1.276-.417a34 34 0 0 1
 12.072-1.341Zm-13.061-2.11a23 23 0 0
 1-2.11.768l-.547.157c-2.761.768-5.56.977-8.269.677v2.826c2.995.3
 6.081.039
 9.142-.821l.547-.156c.234-.078.482-.156.716-.234.469-.156.938-.339
 1.393-.521l-.872-2.683Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://en.oceanbase.com/legal/service-agreem'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/oceanbase/oceanbase/blob/9'''

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
