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


class RookIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rook"

    @property
    def original_file_name(self) -> "str":
        return "rook.svg"

    @property
    def title(self) -> "str":
        return "Rook"

    @property
    def primary_color(self) -> "str":
        return "#2AC6EA"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Rook</title>
     <path d="M1.8246 0c-.4424 0-.774.3685-.774.774v6.1198c0
 .4424.3685.7747.774.7747H5.88c.4424 0 .774-.3323.774-.7747
 0-.4424-.3684-.774-.774-.774H2.562V1.548h2.544v1.2903c0
 .2212.0736.4056.221.553.1475.1475.3687.2218.553.2218h4.092c.4425 0
 .7749-.3692.7749-.7748V1.5481H13.29v1.2903c0
 .4424.3692.7748.7747.7748h4.092c.2213 0
 .4056-.0743.553-.2218.1476-.1474.2211-.3686.2211-.553V1.5481h2.544V6.083H18.12c-.4424
 0-.7748.3685-.7748.774 0 .4424.3692.774.7748.774h4.092c.1843 0
 .4055-.0735.553-.221.1475-.1474.221-.3686.221-.553V.774c0-.4055-.3689-.7371-.6638-.774h-4.092c-.4425
 0-.7741.3685-.7741.774v1.2904h-2.544V.774c0-.4424-.3685-.7741-.774-.7741h-4.092c-.4425
 0-.7741.3685-.7741.774v1.2904H6.6914V.774C6.6914.3317 6.3222 0 5.9167
 0ZM1.788 9.069c-.4424 0-.774.3686-.774.774v8.8113C1.0138 21.6037
 3.4101 24 6.3594 24h11.281c2.9493 0 5.3457-2.3963
 5.3457-5.3457V9.8431c0-.4424-.3686-.774-.774-.774zm.774
 1.5114h18.8762v8.074c0 2.1013-1.6962 3.7975-3.7976
 3.7975H6.3595c-2.1014 0-3.7976-1.6962-3.7976-3.7976zm9.4377
 2.544c-1.8802 0-3.4281 1.5486-3.4281 3.4288v2.6541c0
 .4424.3685.7741.774.7741h5.309c.4424 0
 .774-.3685.774-.774v-2.6542c0-1.8802-1.5487-3.4288-3.4289-3.4288zm-.0367
 1.4746c1.0691 0 1.9175.8484 1.9175
 1.9175v1.9168h-3.8343v-1.9168c0-1.0691.8477-1.9175 1.9168-1.9175z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.linuxfoundation.org/legal/tradema'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/rook/artwork/blob/d252db9f'''

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
