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


class TidbIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tidb"

    @property
    def original_file_name(self) -> "str":
        return "tidb.svg"

    @property
    def title(self) -> "str":
        return "TiDB"

    @property
    def primary_color(self) -> "str":
        return "#DC150B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>TiDB</title>
     <path d="M12 0 1.609 6.001v11.998L11.999
 24l10.393-6.001V6.001ZM8.535 17.999v-7.998L5.07 12V8L12 4l3.462
 2-3.464 2.001v12Zm6.93 0v-7.997l3.464-2v7.997z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.pingcap.com/tidb-brand-guidelines'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.pingcap.com/tidb-brand-guidelines'''

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
