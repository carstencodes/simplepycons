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


class GooglePhotosIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googlephotos"

    @property
    def original_file_name(self) -> "str":
        return "googlephotos.svg"

    @property
    def title(self) -> "str":
        return "Google Photos"

    @property
    def primary_color(self) -> "str":
        return "#4285F4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Photos</title>
     <path d="M12.678 16.672c0 2.175.002 4.565-.001
 6.494-.001.576-.244.814-.817.833-7.045.078-8.927-7.871-4.468-11.334-1.95.016-4.019.007-5.986.007-1.351
 0-1.414-.01-1.405-1.351.258-6.583 7.946-8.275
 11.323-3.936L11.308.928c-.001-.695.212-.906.906-.925 6.409-.187 9.16
 7.308 4.426 11.326l6.131.002c1.097 0 1.241.105 1.228 1.217-.223
 6.723-7.802 8.376-11.321 4.124zm.002-15.284l-.003 9.972c6.56-.465
 6.598-9.532.003-9.972zm-1.36 21.224l-.001-9.97c-6.927.598-6.29
 9.726.002 9.97zM1.4
 11.315l9.95.008c-.527-6.829-9.762-6.367-9.95-.008zm11.238 1.365c.682
 6.875 9.67 6.284 9.977.01z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://partnermarketinghub.withgoogle.com/br'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://partnermarketinghub.withgoogle.com/br'''

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
