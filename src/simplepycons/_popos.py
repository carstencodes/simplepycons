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


class PoposIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "popos"

    @property
    def original_file_name(self) -> "str":
        return "popos.svg"

    @property
    def title(self) -> "str":
        return "Pop!_OS"

    @property
    def primary_color(self) -> "str":
        return "#48B9C7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Pop!_OS</title>
     <path d="M12 0C5.372 0 0 5.373 0 12c0 6.628 5.372 12 12 12 6.627
 0 12-5.372 12-12 0-6.627-5.373-12-12-12ZM9.64 2.918c1.091-.026
 1.548.229 2.182.635a4.459 4.459 0 0 1 1.902 2.764c.254 1.141.178
 2.029-.127 2.664v.05c-.609 1.294-1.622 2.335-3.043 2.842l1.217
 3.172c.228.583.432 1.192.254
 1.75-.177.558-.989.736-1.572.127-1.116-1.192-4.871-8.702-5.15-9.26-.279-.558-.584-1.016-.584-1.574.026-.837
 1.318-1.7 1.953-2.131.634-.431 1.877-1.014 2.968-1.039Zm-.996
 2.311c-.789.022-.358 1.669-.197 2.129.178.507.661 1.572 1.193
 2.105.127.127.254.229.407.254.152.027.457-.127.584-.33a.932.932 0 0 0
 .15-.559 3.232 3.232 0 0
 0-.049-1.216c-.228-.787-.711-1.548-1.346-2.055-.127-.102-.279-.229-.457-.279a.901.901
 0 0 0-.285-.049Zm8.414 2.027a2.283 2.283 0 0 1
 1.588.636c.305.279.33.582.229.963-.102.38-.457 1.194-.736 1.777l-.709
 1.344c-1.37 2.435-1.649 2.689-2.03
 2.537-.456-.178-.304-2.614.127-5.582.127-.812.329-1.217.557-1.42.171-.152.6-.248.975-.254l-.001-.001Zm-1.859
 8.332c.554.011.789.7.656 1.232a.861.861 0 0
 1-.379.559c-.203.127-.685.127-.965-.102-.278-.228-.33-.609-.254-.914.076-.304.331-.635.686-.736a.757.757
 0 0 1 .256-.039Zm-8.604 2.805h10.809c.52 0 .938.419.938.939v.074c0
 .52-.418.94-.938.94H6.595a.936.936 0 0
 1-.937-.94v-.074c0-.52.417-.939.937-.939Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/system76/brand/blob/7a3174'''

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
