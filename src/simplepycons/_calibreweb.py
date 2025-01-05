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


class CalibrewebIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "calibreweb"

    @property
    def original_file_name(self) -> "str":
        return "calibreweb.svg"

    @property
    def title(self) -> "str":
        return "Calibre-Web"

    @property
    def primary_color(self) -> "str":
        return "#45B29D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Calibre-Web</title>
     <path d="M13.736.083q4.9353-.6785 5.5252 4.1915-1.104
 5.4862-6.4778
 7.1446-1.3131.3981-2.6673.1905-.409-.133-.6668-.4763a3.91 3.91 0 0 1
 0-1.7147q4.0727.4425
 6.4778-3.0484.8668-1.3161.5715-2.8578-.5576-1.2044-1.9052-1.1432-2.7075.4504-4.382
 2.6674-3.9135 5.7548-2.4768 12.5745 1.59 5.4391 6.954 3.5246
 1.458-.7474 2.6674-1.81 1.627.6834.8573 2.2864-4.452 3.9011-9.8119
 1.4289-3.1384-2.512-3.5247-6.573-.858-7.33 3.62-13.1462Q10.673.9268
 13.736.083" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/janeczku/calibre-web/blob/'''

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
