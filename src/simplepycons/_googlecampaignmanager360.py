#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class GoogleCampaignManagerThreeHundredAndSixtyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googlecampaignmanager360"

    @property
    def original_file_name(self) -> "str":
        return "googlecampaignmanager360.svg"

    @property
    def title(self) -> "str":
        return "Google Campaign Manager 360"

    @property
    def primary_color(self) -> "str":
        return "#1E8E3E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Campaign Manager 360</title>
     <path d="M15.8203 0c-2.093.0002-4.1858.7997-5.7832 2.3965-1.3364
 1.3364-2.112 3.0208-2.33 4.7617a8.731 8.731 0 0 1
 .4726-.0137c1.7849-.0001 3.5658.5466 5.0763
 1.6387-.2066-.8822.0681-1.8261.7127-2.4707 1.046-1.0459 2.7113-.9977
 3.7149.0059 1.0827 1.0826 2.8372 1.0826 3.92 0 1.0826-1.084
 1.0826-2.8392 0-3.922C20.006.7992 17.9133-.0001 15.8202 0Zm7.0781
 4.0781c.0785.929-.234 1.8855-.9414 2.5938-.9808.9809-2.438
 1.2037-3.6386.6738.3115.9383.065 1.9896-.6329
 2.6875-.9913.9913-2.6633
 1.0662-3.7255.0039-.0173-.0172-.0293-.0352-.046-.0527l-.003.002c-3.1988-3.142-8.3393-3.1251-11.5165.0507-3.1935
 3.1935-3.1935 8.373 0 11.5664 1.1618 1.1618 3.0453 1.1618 4.207 0
 1.1618-1.1618.8689-2.7562-.293-3.918-.9353-.9354-1.1225-2.5928-.0058-3.7109.9095-.9095
 2.5376-1.1696 3.7266-.0078.0726.0726.1477.1405.2246.2031 3.208 2.9849
 8.2258 2.9155 11.3496-.207 2.68-2.679 3.1113-6.7548
 1.295-9.8848zM10.7246 15.1992c.2151.8774-.0348 1.8317-.7012
 2.498-.6718.672-1.6786.924-2.5918.6583.2105.3921.3471.8085.3926
 1.2363.088.8272-.1925 1.6886-.8691 2.3652-.7565.7566-1.781
 1.0896-2.7735 1 3.1157 1.7478 7.1304 1.2962 9.7813-1.3535
 1.337-1.3364 2.1102-3.0208
 2.3281-4.7617-1.946.1045-3.9194-.4446-5.5664-1.6426z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://developers.google.com/doubleclick-adv'''

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