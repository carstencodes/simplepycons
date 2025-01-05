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


class FedoraIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fedora"

    @property
    def original_file_name(self) -> "str":
        return "fedora.svg"

    @property
    def title(self) -> "str":
        return "Fedora"

    @property
    def primary_color(self) -> "str":
        return "#51A2DA"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Fedora</title>
     <path d="M12.001 0C5.376 0 .008 5.369.004
 11.992H.002v9.287h.002A2.726 2.726 0 0 0 2.73 24h9.275c6.626-.004
 11.993-5.372 11.993-11.997C23.998 5.375 18.628 0 12 0zm2.431
 4.94c2.015 0 3.917 1.543 3.917 3.671 0 .197.001.395-.03.619a1.002
 1.002 0 0 1-1.137.893 1.002 1.002 0 0 1-.842-1.175 2.61 2.61 0 0 0
 .013-.337c0-1.207-.987-1.672-1.92-1.672-.934 0-1.775.784-1.777
 1.672.016 1.027 0 2.046 0 3.07l1.732-.012c1.352-.028 1.368 2.009.016
 1.998l-1.748.013c-.004.826.006.677.002 1.093 0 0 .015 1.01-.016
 1.776-.209 2.25-2.124 4.046-4.424 4.046-2.438
 0-4.448-1.993-4.448-4.437.073-2.515 2.078-4.492
 4.603-4.469l1.409-.01v1.996l-1.409.013h-.007c-1.388.04-2.577.984-2.6
 2.47a2.438 2.438 0 0 0 2.452 2.439c1.356 0 2.441-.987
 2.441-2.437l-.001-7.557c0-.14.005-.252.02-.407.23-1.848 1.883-3.256
 3.754-3.256z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://fedoraproject.org/wiki/Legal:Trademar'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://docs.fedoraproject.org/en-US/project/'''

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
